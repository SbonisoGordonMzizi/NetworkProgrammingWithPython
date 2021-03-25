import socket
import argparse


def dns_lookup(args):
    if args.reverse:
        for ipaddress in args.add:
            print(socket.gethostbyaddr(ipaddress))
    else:
        for hostname in args.add:
            print(f"{hostname} ==> {socket.gethostbyname(hostname)}")


if __name__ == "__main__":
    argparseObject = argparse.ArgumentParser(description="argparse object for DNS lookup")
    argparseObject.add_argument("add", type=str, nargs="+")
    argparseObject.add_argument("-r", "--reverse", help="provide ip address to get domain name", action="store_true")
    args = argparseObject.parse_args()

    dns_lookup(args)
