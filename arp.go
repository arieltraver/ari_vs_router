/*
Writing an arp cache poison using Go.
Also using Google's "go packet" library.
https://pkg.go.dev/github.com/google/gopacket 
*/
package main;
import (
	"fmt"
	"errors"
	"syscall"
	"net"
	"time"
	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
	"github.com/google/gopacket/pcap"
)

