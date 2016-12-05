# CnPiAwareKafka_20161204_1945

Push PiAware data from a PiAware system to Kafka in real time.

On a system running PiAware, there seems to be three ways of getting
PiAware data:

  1. Subdirectory /run/dump1090-fa/

    This subdirectory contains 120 files in the form history_0.json to
    history_119.json.  Each file contains a minute-by-minute summary of
    PiAware data.

  2. http://localhost:8080/data/aircraft.json

    Current state of system, also in JSON format.  Seems to be more detailed
    than #1

  3. "Firehose" of data from radio receiver.  I have yet to figure out
    how access this.

This software currently uses #2.



    


    
