# How To Build

- Install InnoSetup from [Official InnoSetup Site](https://jrsoftware.org/isdl.php#stable)
- Download `"Tor Expert Bundle"` from [Official TorProject Site](https://www.torproject.org/download/tor/)
- Extract tor-expert-bundle zip file. Move all `*.exe` and `geoip*` files to a folder named `tor` in root directory of this project.

``` Bash
├── build.iss
├── files
│   ├── clean.bat
│   ├── config.txt
│   ├── icon.ico
│   ├── start.bat
│   ├── TorClean.lnk
│   └── Tor.lnk
└── tor
    ├── geoip
    ├── geoip6
    ├── lyrebird.exe
    ├── snowflake-client.exe
    ├── tor.exe
    └── tor-gencert.exe
```

- Open `build.iss` with `InnoSetup` and Compile. Installer executable will be created in `dist` directory.
