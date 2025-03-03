            ------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------
                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~
                                                        ~ _____ _               ~
                                                        ~|  ___| | _____      __~
                                                        ~| |_  | |/ _ \ \ /\ / /~
                                                        ~|  _| | | (_) \ V  V / ~
                                                        ~|_|   |_|\___/ \_/\_/  ~
                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~
            ------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------
            Note: Flow can only be run as a Python script from a terminal at the moment. That will change soon.
            Dependencies: pyexcel, statistics, os, shutil
            ------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------
            Oscar displays 95% flow limit, 99.5% flow limit, and a graph showing flow limits throughout the night but sometimes
            it's helpful to take a closer look at your CPAP's flow limitation data. Flow works with Oscar, analyzing flow 
            limitation data from an exported detail report to generate a report containing the following values for each date
            in the Oscar detail report: 

                                        Date
                                        Total Flow Limitations
                                        # of flow limitations above 0.05
                                        # of flow limitations above 0.10
                                        # of flow limitations above 0.20
                                        # of flow limitations above 0.30
                                        Average flow limitation
                                        Max flow limitation

            ------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------
            Steps: 
                        1. Export the "details" report for your target timeframe in Oscar.
                        2. Navigate to your Oscar folder.
                        3. Run flow.py from your preferred terminal.
                        4. Copy/paste the Windows filepath for the Oscar details report into the terminal when prompted.
                        5. Do the same for the Oscar folder path. 
                        6. A flow limitation report will be generated and sent to your Oscar folder.
            ------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------

            Related resources:

                        Install Oscar: https://www.sleepfiles.com/OSCAR/
                        Oscar guide: https://www.apneaboard.com/wiki/index.php/OSCAR_-_The_Guide

            ------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------