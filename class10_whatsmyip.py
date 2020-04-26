from subprocess import check_output as call
#!/usr/local/bin/python3
ip = bytes.decode(
    call(
        'dig +short myip.opendns.com @resolver1.opendns.com',
        shell=True
    )
).strip()
 
print("My WAN IP is {}".format(ip))