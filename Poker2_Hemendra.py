class Pokerb:

    # Using init function Declaration and Initialization of all variables
    def __init__(self):

        self.data = 0
        self.totalcount = 0
        self.rank = {"nothing_count":0,"onepair_count":0,"twopairs_count":0,"threeofakind_count":0,
                     "straight_count":0,"flush_count":0,"fullhouse_count":0,"fourofakind_count":0,
                     "straightflush_count":0,"royalflush_count":0}

    # Function for Exception Handling while doing File Operations
    def verify_data(self):

        try:
            self.data = open("C:\\Users\\Hemendra\\Desktop\\poker-hand.data","r")
        except :
            print("File not found to read")

    # Function for Counting Logic implementation
    def hands_ranking(self):

        for line in self.data:
            fileds = line.split(",")
            hand_rank = int(fileds[-1])

            if hand_rank == 0:
                self.rank["nothing_count"] += 1
            elif hand_rank ==1:
                self.rank["onepair_count"] += 1
            elif hand_rank ==2:
                self.rank["twopairs_count"] += 1
            elif hand_rank == 3:
                self.rank["threeofakind_count"] += 1
            elif hand_rank ==4:
                self.rank["straight_count"] += 1
            elif hand_rank ==5:
                self.rank["flush_count"] += 1
            elif hand_rank == 6:
                self.rank["fullhouse_count"] += 1
            elif hand_rank ==7:
                self.rank["fourofakind_count"] += 1
            elif hand_rank ==8:
                self.rank["straightflush_count"] += 1
            else:
                self.rank["royalflush_count"] += 1

    # Print List of counter values
        print("List of HandRank Counts\n",self.rank.values())

        # For loop for displaing all counter values as well total count
        print("\nHandRank : Count for each handrank \n")
        for name,count in self.rank.items():
            print(name," : ",count)
            self.totalcount +=count

        print("\nTotal Count: ",self.totalcount)

o = Pokerb()
o.verify_data()
o.hands_ranking()

