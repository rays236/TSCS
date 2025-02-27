import traci 
import traci.constants as tc 

# Specify "--num-clients" --> "2" for two users . User 1 is Client 1 and User 2 is Client 2, and so on
traci.start([
    "sumo-gui",
    "-c", "/Users/roshanthapa/Sumo/2025-02-23-22-11-51/osm.sumocfg", \ # Modify your location to .sumocfg file 
    "--num-clients", "2"], port=8813)

# Client 1 is always this server. Set to 1
traci.setOrder(1)

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    # More traci commands
traci.close()
