FAQ
****

What is this?
-------------
An interface to make calls to the pingme server.  This allows you to send arbitrary notifications to your android phone, provided you have the android application installed.

How does this work?
-------------------

It is just sending post calls to the server with the correct arguments.  If you want to make your own calls to the server you can do so with this structure.
::

    POST
    Header
    Content-Type: application/json
    Body
    {
    "device_id":["device_ids"],
    "message":"message"
    }

An example curl request would look like this ::

    curl -X POST -H "Content-Type: application/json" -d '{"device_id":["PUTIDHERE"],"message":"TEST MESSAGE"}' https://ping.blu3f1re.com/ping/

To get a device id you must download the Android app from the app store.

Why?
----
I wrote this for 2 use cases.  I wanted a way to ping my phone when a long running job completed on my servers.::

    cp -r reallybigdirectory/ newfilesystem/ ; pingme

Also I thought it would be useful for sending myself alerts for some of the scripts I write.  Before I was using emails but I would not notice them for hours.  Notifications are much easier to see quickly.  Any script that can make web requests can ping your phone.
