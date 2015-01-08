How to use
**********

First you must download the Android application at


The app will guide you through registering your device against the pingme server.  Once you have your device id, you can email it to yourself for easy portability.  If you want to ping your phone from a server then as long as you can run python all you need to do is::

    pip install pingme

to get the client.  If you want to make the web calls yourself, or are planning on using this from within a script or application here is the format the server expects.::

    curl
    -X POST
    -H "Content-Type: application/json"
    -d
    '{
        "device_id":["PUTIDHERE"],
        "message":"TEST MESSAGE"
    }'
    https://ping.blu3f1re.com/ping/
