class Poker:

    def handrank(self):

    #Declaration and Initialization of variables for counters
        total_count = 0
        nothing_count = 0
        onepair_count = 0
        twopairs_count = 0
        threeofakind_count = 0
        straight_count = 0
        flush_count = 0
        fullhouse_count = 0
        fourofakind_count = 0
        straightflush_count = 0
        royalflush_count = 0

    #Exception Handling for File Operations
        try:
            data = open("C:\\Users\\Hemendra\\Desktop\\poker-hand.data","r")

        except :
            print("File not found: ")

    # Logic implementation for counting each handrank
        #Reading each line from the file data and splitting to get the last index element
        for line in data:
            fileds = line.split(",")
            hand_rank = int(fileds[-1])

        #Increasing respective counters if matches
            if hand_rank == 0:
                nothing_count += 1
            elif hand_rank ==1:
                onepair_count += 1
            elif hand_rank ==2:
                twopairs_count += 1
            elif hand_rank == 3:
                threeofakind_count += 1
            elif hand_rank ==4:
                straight_count += 1
            elif hand_rank ==5:
                flush_count += 1
            elif hand_rank == 6:
                fullhouse_count += 1
            elif hand_rank ==7:
                fourofakind_count += 1
            elif hand_rank ==8:
                straightflush_count += 1
            else:
                royalflush_count += 1
            total_count +=1

    #Print all counters to Display Output
        print("Nothing_count : ",nothing_count)
        print("Onepair_count : ", onepair_count)
        print("Twopairs_count : ", twopairs_count)
        print("Threeofakind_count : ", threeofakind_count)
        print("Straight_count : ", straight_count)
        print("Flush_count : ", flush_count)
        print("Fullhouse_count : ",fullhouse_count)
        print("Fourofakind_count : ", fourofakind_count)
        print("Straightflush_count : ", straightflush_count)
        print("Royalflush_count : ", royalflush_count)
        print("Total_count : ", total_count)

        data.close()

o = Poker()
o.handrank()