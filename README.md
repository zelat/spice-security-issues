Spice-Security-Issues
===
I found a security issue on spice Server when I was fuzzing Spice server.

Introduce
===
  A handshake is required before the spice-server and spice-client can establish communication, spice-client will send a request containing some information that the server needs. This TCP request requires only host and port. So I constructed a malformed TCP packet that caused the vm to crash and the QEMu-KVM process to be restarted.
  
Repeat steps
===
  1. Send a malformed TCP packet(Observe the packets intercepted by Wirshark)
  
  2. check qemu-kvm process && kvm instance state
  
  3. Check libvirt's log that the virtual machine crashed
  
  
