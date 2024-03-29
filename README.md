# BBB Profibus Slave
Profibus DP Slave on a Beablebone Black SBC running on Ti-RTOS

This repo contains instructions to run a Profibus slave on a Beaglebone Black single board computer. No binaries and not all code are provided here due to the export control restrictions of the original Profibus slave package from Texas Instruments (everything is freely available but it can only be downloaded from TI's website after signing up, agreeing to the export conditions and getting the required approval).

[Beaglebone Black](https://beagleboard.org/black) (BBB) is Single Board Computer (SBC) with some advanced features. It runs on a Texas Instruments Sitara(TM) [AM335x processor](http://www.ti.com/processors/sitara-arm/am335x-cortex-a8/overview.html), which is an ARM Core A8 together with some ancillary hardware, including what TI calls PRU-ICSS (programmable real-time subsystem for industrial communication protocols), a fancy name for a two-core microcontroller with nice real time capabilities.

## Motivation and background

[Profibus](https://en.wikipedia.org/wiki/Profibus) is a networking technology standard, more than just a protocol because it especifies both the communication protocol at a theoretical level and most hardware particularities like cable or connectors. It is widely used in many industries around the world to connect different field devices together, mainly PLCs and other industrial controllers and computers to sensors and other data acquisition devices.

Started in the '80s-90s it is still quite popular, even for new facilities. It was first developed by the *Bundesministerium für Bildung und Forschung* (German Ministry of Education and Research and later embraced and supported by the German conglomerate Siemens AG. Together with Profinet (a similar standard that runs over Ethernet), it is now actively promoted by Profibus&Profinet Iternational (or [PI](https://www.profibus.com/)), a kind of foundation that styles itself as *the most influential interest group in the field of industrial communication*.

Being intended for mission critical infraestructure, Profibus is not a good fit for at-home or hobby projects. Of the thousands that are listed as compliant with the standard, even the most basic devices will go for no less than 500-1000$US. There is a reason for this high cost: if you want your new product to comply with the standard you need to certify it and pay the fees and since most users are big companies, they can afford to pay and you end up lock in a high-cost cycle. On the hardware front, Profibus has certain requirements for hard real time that made a custom ASIC the default choice until recently.

Early this decade, Texas Instruments launched their low cost Sitara family of processors with the automation industry as its main target. Among the products they brought to the market we can find several interesting development boards for a very low cost (some of them [less than 200$US](http://www.ti.com/tool/tmdsice3359)).

These boards are ideal for product development but also for testing or commisioning of industrial networks. In a typical scenario for a system integrator, there are several suppliers of equipment that you need to bring together to a Distributed Control System (for monitoring, data acquisition and control) and you need tools to debug their communication links prior to commissioning.

But 200$ is quite a high mark for the average home user. If you want to put together your own Profibus network for educational purposes or you have a second-hand PLC you want to play with, it would still take a hefty pile of money.

That's where the Beaglebone Black comes into the picture: for 45-55$ for the SBC and 5$ for an RS-485 to TTL converter you can have your own Profibus slave (or master hopefully).

## Let's go for it!

Unfortunately, binary files have a commercial license and cannot be made availble here. So if you want to run the Profibus Slave you'll have to setup the environment, make some modifications on TI's Platform Development Kit (PDK), and compile it together with the Profibus stack and sample code. If you are not familiar with TI RTOS (a minimalist real time operating system for TI's Sitara processors) but you know your way around Eclipse or a similar development environment and makefiles and the like, it should not take longer than an afternoon to setup everything. If you did not even understand the previous sentence, no worries, I'm planning to give quite detailed instructions, but it can take significantly longer depending on your skills.

Unfortunately, I did not have time to write and explain everything yet, but if you want to have a Profibus Slave (or Master) running on your BBB just head to this two threads: [1](https://e2e.ti.com/support/processors/f/791/p/830896/3080938?tisearch=e2e-sitesearch&keymatch=profibus%2520linux#pi320966=1), [2](https://e2e.ti.com/support/processors/f/791/t/830322?tisearch=e2e-sitesearch&keymatch=profibus%2520master). 

If you still have trouble you are welcome to post an issue.

## Credits and disclaimer

As you'll see if you deep digger into the documentation, most of the credit belongs to TI. Their processors and tools are greatly appreciated.
