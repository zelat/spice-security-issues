Spice-Security-Issues
===
I found a security issue on spice Server when I was fuzzing Spice server.

Introduce
===
  A handshake is required before the spice-server and spice-client can establish communication, spice-client will send a request containing some information that the server needs. This TCP request requires only host and port. So I constructed a malformed TCP packet that caused the vm to crash and the QEMu-KVM process to be restarted.
  
How to run
===
#1. Send a malformed TCP packet(Observe the packets intercepted by Wirshark)
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-29_105113.png)
#2. check qemu-kvm process && kvm instance state
  
  Before sending a malformed TCP packet<br>
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-29_112749.png)
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-29_110811.png)
  After sending a malformed TCP packet <br>
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-29_113008.png)

#3. Check libvirt's log that the virtual machine crashed
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-28_170135.png)
#4. Observe the virtual machine through virt-manage, found that the virtual machine has been restarted
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-29_114745.png)

Vulnerability Code
===
  Code Address: https://gitlab.freedesktop.org/spice/spice/-/blob/master/server/red-stream.cpp<br>
  Function：async_read_handler 
  Description: The function async_READ_handler caused a deadlock while processing the data stream.
  ![](https://github.com/zelat/spice-security-issues/raw/master/Pictures/2020-06-29_124526.png)
  
Related component version
===
  Centos: Linux version 3.10.0-957.10.2.el7.x86_64<br>
  Qemu-kvm: QEMU emulator version 2.10.0(qemu-kvm-ev-2.10.0-21.el7_5.7.1)<br>
  Spice-server rpm: spice-server-0.14.0-6.el7_6.1.x86_64<br>
