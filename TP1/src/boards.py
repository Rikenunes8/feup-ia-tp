EC = 0
VC = 8
BC = 9

# List of boards to display
boardsULM = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

initBoards =( # 0
             [[EC, EC, BC, BC, EC, EC],
              [EC, EC, EC, EC, EC, BC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 1
             [[BC, BC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 2
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, BC],
              [EC, EC, EC, EC, EC, EC],
              [EC, BC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 3
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC],
              [VC, BC, EC, EC, EC, EC]],
            # 4
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC],
              [VC, EC, EC, BC, EC, EC]],              
            # 5
             [[EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 6
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC],
              [EC, EC, EC, BC, BC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 7
             [[EC, EC, EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, EC, EC, EC, BC, EC],
              [BC, EC, EC, EC, EC, EC, EC, EC],
              [BC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC, EC]],
            # 8
             [[EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, BC, BC]],
            # 9
             [[BC, BC, BC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, BC, EC, EC, EC, EC, EC, EC]],
            # 10
             [[BC, BC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, BC, BC]],
)