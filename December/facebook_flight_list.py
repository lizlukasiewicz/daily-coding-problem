"""
given an unordered list of flights taken by someone, represented as (origin, destination) pairs,
and a starting airport, compute persons itinerary.
example list of flights:: [('SFO', 'HKO'), ('YYZ','SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
     && starting point :: 'YUL' 
            return list:: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    list of flights:: [('SFO', 'COM'), ('COM', 'YYZ')]
    && starting point:: 'COM'
                        return null

LEXOGRAPHICALLY SMALLER

"""
def itinerary(flights: list, begin: str):
    itinerary=[]
    start=begin
    for x in range(len(flights)):

        options=[point for point in flights if point[0]==start]

        if len(options) <= 0:
            print('null')
            return None

        itinerary.append(start)
        n_connect=sorted([second[1] for second in options])
        start=n_connect[0]
    
    itinerary.append(start)
    print(itinerary)


ex_flight=[('SFO', 'HKO'), ('YYZ','SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
star='YUL'
ex2=[('SFO', 'COM'), ('COM', 'YYZ')]
star2='COM'
ex3=[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
star3='A'
itinerary(ex_flight, star)
itinerary(ex2, star2)
itinerary(ex3, star3)