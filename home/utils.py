from datetime import datetime, time

def is_restaurant_open():
    now = datetime.now()
        current_weekday = now.weekday()  # Monday is 0, Sunday is 6
            current_time = now.time()
            
                # Example: Open 9 AM to 10 PM Monday-Saturday, 10 AM to 8 PM Sunday
                    if current_weekday == 6:  # Sunday
                            open_time = time(10, 0)   # 10:00 AM
                                    close_time = time(20, 0)  # 8:00 PM
                                        else:  # Monday-Saturday
                                                open_time = time(9, 0)    # 9:00 AM
                                                        close_time = time(22, 0)  # 10:00 PM
                                                        
                                                            return open_time <= current_time < close_timefrom datetime import datetime, time
                                                            
                                                            def is_restaurant_open():
                                                                now = datetime.now()
                                                                    current_weekday = now.weekday()  # Monday is 0, Sunday is 6
                                                                        current_time = now.time()
                                                                        
                                                                            # Example: Open 9 AM to 10 PM Monday-Saturday, 10 AM to 8 PM Sunday
                                                                                if current_weekday == 6:  # Sunday
                                                                                        open_time = time(10, 0)   # 10:00 AM
                                                                                                close_time = time(20, 0)  # 8:00 PM
                                                                                                    else:  # Monday-Saturday
                                                                                                            open_time = time(9, 0)    # 9:00 AM
                                                                                                                    close_time = time(22, 0)  # 10:00 PM
                                                                                                                    
                                                                                                                        return open_time <= current_time < close_time                fail_silently                                                                                                                                                                                