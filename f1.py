my_space = SpaceNetwork(level=1)
earth = SpaceEntityNotSat("Earth", 0)
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
sat3 = Satellite("Sat3", 300)
sat4 = Satellite("Sat4", 400)
sat5 = Satellite("Sat5", 450)

sates = [ sat1, sat2, sat3, sat4,sat5]


def smart_send_packet(packet: Packet, satellites: list):
    max_range = 150
    packet = packet
    satellites = satellites
    sat_source = packet.sender
    dist_source = packet.sender.distance_from_earth
    if packet.receiver.distance_from_earth - dist_source <= max_range:
        try:
             attempt_transmission(packet)
        except:
            print("Transmission failed")
    else:
        trip = {packet.receiver}
        ## selecting satellites for trip
        while packet.receiver.distance_from_earth - dist_source > max_range:
            target = packet.receiver
            difference_range = target.distance_from_earth - max_range
            sates_in_range = []
            for sati in satellites:
                if target.distance_from_earth > sati.distance_from_earth >= difference_range:
                    sates_in_range.append(sati)
            sates_in_range.sort(key=lambda sat: sat.distance_from_earth)
            hope = sates_in_range[0]
            trip.add(hope)
        trip.add(sat_source)
        ## casting 'trip' from set to list
        trip = list(trip)
        trip.sort(key=lambda sat: sat.distance_from_earth)
        ## creating packets
        packets = []
        for i in range(len(trip)):
            if i == 0:
                packet.sender = trip[1]
                packets.append(packet)
            else:
                re_packet = RelayPacket(packets[i-1],trip[i],trip[i-1])
                packets.append(re_packet)
        print(packets[-1])

        ## sending packet:
        try:
             attempt_transmission(packets[-1])
        except:
            print("Transmission failed")
