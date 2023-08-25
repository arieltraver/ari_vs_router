# Ari VS Router
## A quest to enable SSH on my TP-link AX3000, by whatever means necessary
From the TP Link website: *"SSH Services on the TP-Link products are only available for TP-Link apps. Other SSH clients cannot access to TP-Link products or adjust their settings with command lines. So please rest assured that the SSH will never cause any safety issues on your device."*
<p>We will see about that!</p>

### Current endeavor
<p>The Archer AX3000 allows SSH connections from the "Tether" app on mobile devices. Its port 22 is open, and prompts for username/password. One plan of attack is to use the tool Hydra to try and brute force the credentials. However, just because username/password authentication is enabled, doesn't mean there are any existing credentials. I will have to try this and see. (IN PROGRESS)</p>
<p>Another angle would involve capturing outgoing packets from the Tether app, either by MITM or by using an emulator, and see if I can obtain a cleartext password. If the Router uses key pairs, then this will not work, but I may as well give it the old college try. If the Tether app contains a private key, I may be able to find it in the source code if it's not well-protected, especially if I use an emulator. (SPECULATION)</p>
<p>I have also purchased two USB drives online. I plan to use one of these to flash OpenWRT firmware onto this router, using the guide below to help pick the right version. This is my backup plan in case I do not manage to get root priveleges on the current installation.(AWAITING USB STICKS)</p>
<p>I'll turn the other USB stick into a rubber duck, assuming it contains the Phison 2303 chipset (the model is supposed to, but it may ship with a later version). The chance of this router having a keyboard circuit is next to none, but I will enjoy having a rubber duck if I can pull it off.</p>


### Resources
* [portscan tutorial](https://stackoverflow.com/questions/7541056/pinging-an-ip-range-with-scapy)
* [arp spoofing tutorial](https://www.geeksforgeeks.org/python-how-to-create-an-arp-spoofer-using-scapy/)
* [reverse engineering TP-link firmware](https://thunderysteak.github.io/tl-wa901nd-basic-re)
* [channels and antennae](https://www.reddit.com/r/openwrt/comments/svnv71/devices_similar_to_tplink_ax3000_with_openwrt/)
* [open wrt](https://openwrt.org/)
* [forum discussion of same mission, no answer](https://community.tp-link.com/us/home/forum/topic/220972)
* [cracking SSH passwords with Kali, known user](https://www.oreilly.com/library/view/kali-linux-cookbook/9781784390303/4b4ec313-72af-493b-a66d-48fe55304d3f.xhtml)
* [TP link ax-55 firmware download](https://www.tp-link.com/us/support/download/archer-ax55/v1.60/#Firmware_)
* [FTP for USB drive - may be exploitable?](https://www.tp-link.com/us/support/faq/2038/)
* [Brute force SSH username/password](https://www.tutorialspoint.com/how-to-brute-force-ssh-in-kali-linux)