# Tor

## Run

Run "Tor" shortcut and don't close terminal window.
Wait for this message:
"Bootstrapped 100% (done): Done"
which means it is successfully connected to the tor network.

## Use

Set "Socks5" proxy of your software to use this tunnel.
Server IP : 127.0.0.1
Server Port : 49050

## Pass Argument to Run

There is a `C:\Tor\tor.bat` file that handles argument. `Tor.lnk` is a shortcut to this file.  
Add `Tor.lnk` to system PATH and call `tor` from Run (WindowsKey + R) with one of these arguments.

### Different Bridges

By default, tor uses `obfs4` for bridges.  
Pass appropriate argument to `Tor.lnk` to use `snowflake` or `meek` bridges.

### Clean Start

Sometimes tor can not connect to the network. Cleaning Data folder could resolve the issue.  
Run `TorClean.lnk` or pass `clean` as the argument to `Tor.lnk` to delete `C:\Tor\Data\` folder.

### Arguments Overview

```shell
# one of these for obfs4
Tor.lnk
Tor.lnk o
Tor.lnk ob
Tor.lnk obfs4

# one of these for meek
Tor.lnk m
Tor.lnk mk
Tor.lnk meek

# one of these for snowflake
Tor.lnk s
Tor.lnk sf
Tor.lnk snow
Tor.lnk snowflake

# clean data folder
TorClean.lnk
Tor.lnk clean

# change identity. make sure tor is running
Tor.lnk new
```
