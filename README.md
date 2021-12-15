# read-directory-info
read-directory-info

### Description

This script helps to return the disk used information in bytes from the mouthpath/folderpath. If the result, has the key as "mount" and value as "true" then it is mouth directory else it can be folder path.


# Creating pyenv

```
python -m venv pyenv
source pyenv/bin/activate
```

# Installing libraries

```
pip install -r requirements.txt
```


# Execution

Example usage: 
```
python3 getdiskusage.py /tmp
```

# Description for parameters
Input information requires mountpath


# Quick Script Execution with Sample Output

```
./runscript.sh > output-sample.txt &
```

# Output

```
-----------Input request information-------
Mouth Path: /tmp
{
    "files": [
        {
            "/tmp/fseventsd-uuid": "8"
        },
        {
            "/tmp/com.google.Keystone": "0"
        },
        {
            "/tmp/powerlog": "0"
        },
        {
            "/tmp/com.apple.launchd.7ka0E27qoc": "0"
        },
        {
            "/tmp/test1": "8"
        },
        {
            "/tmp/test3": "8"
        },
        {
            "/tmp/test2": "8"
        }
    ],
    "mount": true
}
------Script completed--------
```
## Output file link
[output-sample.txt](output-sample.txt)


# Run unit testing 
```
python3 -m unittest test_getdiskusage
```

## Output of Unit tests
[test-output-sample.txt](test-output-sample.txt)

# Reference

- https://docs.python.org/3/library/glob.html
- https://docs.python.org/3/library/argparse.html
- https://docs.python.org/3/library/subprocess.html







