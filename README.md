# ipfs-tools

This script will automate downloading files from a CID. It will also create a directory with the same name as the CID and download the files there.

## Usage
### Download files in provided CID
```bash
python download.py <CID>
```

Note: The files will be downloaded to `./downloads/<CID>/` directory.

#### List files in the provided CID
```bash
python list.py <CID>
```

Note: You might need to run ipfs daemon as well

## Supporting Notes
### Install ipfs
*Reference:* https://docs-ipfs-tech.ipns.dweb.link/install/command-line/#install-official-binary-distributions

### Start ipfs daemon
```bash
ipfs daemon 
```
#### Access ipfs daemon from browser
    WebUI: http://127.0.0.1:5001/webui


### Download files from a CID using ipfs 
```bash
ipfs get <CID>/<filename> -o <filename>
```
