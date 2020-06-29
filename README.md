Spice-Security-Issues
===
I found a security issue on spice Server when I was fuzzing Spice server.

Introduce
===
  A handshake is required before the spice-server and spice-client can establish communication, spice-client will send a request containing some information that the server needs. This TCP request requires only host and port. So I constructed a malformed TCP packet that caused the vm to crash and the QEMu-KVM process to be restarted.
  
Repeat steps
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


  
  
  
