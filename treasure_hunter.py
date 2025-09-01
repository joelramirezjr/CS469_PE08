class TreasureHunterClass:
    """This class helps figure out how many treasures the hunters can collect.
    
    It uses greedy approach, which means each hunter tries to grab the nearest
    treasure they can reach without looking ahead too much.
    """

    def __init__(self):
        """Set up the class.
        
        We don’t really need to store anything here for this problem,
        but we include it so the class is ready to use.
        """
        pass

    def hunt_treasure(self, arr, n, k): 
        """Work out the maximum number of treasures the hunters can find.
        
        Args:
            arr (list): A list with 'H' for hunters and 'T' for treasures.
            n (int): How many spots are in the list.
            k (int): How far a hunter can reach to grab a treasure.
        
        Returns:
            int: The most treasures the hunters can collect.
        """
        hunters = []
        treasures = []

        # Here we go through the list and save the positions of hunters and treasures
        for i in range(n):
            if arr[i] == 'H':
                hunters.append(i)
            elif arr[i] == 'T':
                treasures.append(i)

        # Start both hunters and treasures from the first one in their lists (they start at zero)
        h, t = 0, 0  
        result = 0

        # Keep checking until we run out of hunters or treasures
        while h < len(hunters) and t < len(treasures):
            if abs(hunters[h] - treasures[t]) <= k:
                # Hunter can reach this treasure, so we count it
                result += 1
                h += 1
                t += 1
            elif treasures[t] < hunters[h]:
                # This treasure is too far left, so they move to the next treasure
                t += 1
            else:
                # This hunter is too far left, move to the next hunter
                h += 1

        return result
