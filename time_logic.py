total_seconds=int(input("Enter total number of seconds:"))  # int(input(" ..... int aldığında yap
hours= total_seconds // 3600                                # // tam ksımı veren bölme   / virgüllü bölme yapar
remaining_seconds= total_seconds % 3600
minutes=remaining_seconds // 60
seconds= remaining_seconds % 60
print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")
                                                            # print(f"..... {variable} ....