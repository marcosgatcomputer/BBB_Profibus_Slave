#!/usr/bin/env python3
#
# Simple pyprofibus example
#
# This example initializes an ET-200S slave, reads input
# data and writes the data back to the module.
#
# The hardware configuration is as follows:
#
#   v--------------v----------v----------v----------v----------v
#   |     IM 151-1 | PM-E     | 2 DO     | 2 DO     | 4 DI     |
#   |     STANDARD | DC24V    | DC24V/2A | DC24V/2A | DC24V    |
#   |              |          |          |          |          |
#   |              |          |          |          |          |
#   | ET 200S      |          |          |          |          |
#   |              |          |          |          |          |
#   |              |          |          |          |          |
#   |       6ES7   | 6ES7     | 6ES7     | 6ES7     | 6ES7     |
#   |       151-   | 138-     | 132-     | 132-     | 131-     |
#   |       1AA04- | 4CA01-   | 4BB30-   | 4BB30-   | 4BD01-   |
#   |       0AB0   | 0AA0     | 0AA0     | 0AA0     | 0AA0     |
#   ^--------------^----------^----------^----------^----------^
#

import pyprofibus
import binascii

master = None
try:
	# Parse the config file.
	config = pyprofibus.PbConf.fromFile("example_sitara.conf")

	# Create a DP master.
	master = config.makeDPM()

	# Create the slave descriptions.
	outData = {}
	for slaveConf in config.slaveConfs:
		slaveDesc = slaveConf.makeDpSlaveDesc()

		# Set User_Prm_Data
		#dp1PrmMask = None   pyprofibus.DpTelegram_SetPrm_Req.DPV1PRM1_REDCFG		
		dp1PrmMask = bytearray((0x40,0x00,0x00))
		print(binascii.hexlify(dp1PrmMask))
		dp1PrmSet  = bytearray((0x40,0x00,0x00))
		print(binascii.hexlify(dp1PrmSet))
		prm_data = slaveConf.gsd.getUserPrmData(dp1PrmMask=dp1PrmMask, dp1PrmSet=dp1PrmSet)
		print("prm_data")
		print(binascii.hexlify(prm_data))
		slaveDesc.setUserPrmData(prm_data)
		print("after prm_data")

		# Register the ET-200S slave at the DPM
		master.addSlave(slaveDesc)

		# Set initial output data.
		outData[slaveDesc.slaveAddr] = bytearray((0x00))

	# Initialize the DPM
	master.initialize()

	# Cyclically run Data_Exchange.
	while True:
		# Write the output data.
		for slaveDesc in master.getSlaveList():
			slaveDesc.setOutData(outData[slaveDesc.slaveAddr])

		# Run slave state machines.
		handledSlaveDesc = master.run()
		#print "running..."
		# Get the in-data (receive)
		if handledSlaveDesc:
			inData = handledSlaveDesc.getInData()
			#print inData
			if inData is not None:
				print "inLoop"
				# In our example the output data shall be a mirror of the input.
				outData[handledSlaveDesc.slaveAddr][0] = inData[0] & 3
				outData[handledSlaveDesc.slaveAddr][1] = (inData[0] >> 2) & 3

except pyprofibus.ProfibusError as e:
	print("Terminating: %s" % str(e))
finally:
	if master:
		master.destroy()
