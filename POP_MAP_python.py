#!/usr/bin/env python3

import poplib, imaplib, getpass

def pop_client():
    pop_object = poplib.POP3("172.30.42.127", 110)
    print(pop_object.getwelcome())
    pop_object.user("ric")
    pop_object.pass_("P4ssw0rd!")

    print(pop_object.list())
    pop_object.quit()

def imap_client():
    imap_object = imaplib.IMAP4("172.30.42.127", 143)
    imap_object.login("ric", "P4ssw0rd!")
    imap_object.select()
    t, l = imap_object.list()
    print("Response code: ", t)
    print(l)
    t, ids = imap_object.search(None, "ALL")
    print("Response code: ", t)
    print(ids)
    t, msg = imap_object.fetch('5', "(UID BODY[TEXT])")
    print(msg)
    imap_object.close()
    imap_object.logout()

if __name__ == "__main__":
    imap_client()
    pop_client()