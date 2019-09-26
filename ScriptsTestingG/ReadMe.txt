!!!Script Testing!!!

These scripts are used to API running on PCNC and Frenetic.
The client hit the Flask server running on pcnc with a Json content.

The PCNC recevies the PCNC data, passes it through Bisimulation and verifies the content. 
If validation is true, the Json content is passed to Frenetic.

In Frenetic, the Json content read and converted to .kat format and the frenetic commands are executed.
