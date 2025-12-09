import sys
import heapq
import math

class Circuit:
    def __init__(self, box: JunctionBox):
        self.boxes = {box}
    
    def add_box_to_circuit(self, box: JunctionBox):
        circuit_to_join = box.circuit
        self.boxes.update(circuit_to_join.boxes)
        
        for other_box in circuit_to_join.boxes:
            other_box.circuit = self
    
    def size(self):
        return len(self.boxes)
    
    def __repr__(self):
        return "Circuit {\n\t" + "\n\t".join(str(box) for box in self.boxes) + "\n}"


class JunctionBox:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

        self.unconnected_boxes: list[tuple[float, JunctionBox]] = []
        self.circuit = Circuit(self)
    
    def add_box(self, other: JunctionBox):
        item = (self.get_distance(other), other)
        heapq.heappush(self.unconnected_boxes, item)

    def get_closest(self):
        return self.unconnected_boxes[0]
    
    def get_distance(self, other: JunctionBox):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def connect_closest(self):
        to_connect = self.get_closest()[1]

        if to_connect.get_closest()[1] != self:
            raise ValueError("Cannot connect: not closest")

        self.circuit.add_box_to_circuit(to_connect)

        heapq.heappop(self.unconnected_boxes)
        heapq.heappop(to_connect.unconnected_boxes)

    def __str__(self):
        return f"<Box at ({self.x}, {self.y}, {self.z})>"

def make_connections(boxes: list[JunctionBox], number: int):
    for i in range(number):
        lowest_distance = boxes[0].get_closest()[0]
        box_to_connect = boxes[0]
        
        for box in boxes:
            distance = box.get_closest()[0]
            if distance < lowest_distance:
                lowest_distance = distance
                box_to_connect = box
        
        box_to_connect.connect_closest()

def get_circuits(boxes: list[JunctionBox]):
    circuits = []
    for box in boxes:
        if box.circuit not in circuits:
            circuits.append(box.circuit)
    return circuits

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

boxes: list[JunctionBox] = []

print("Building Input")
for line in raw_input.split("\n"):
    new_box = JunctionBox(*map(int, line.split(",")))
    for existing_box in boxes:
        existing_box.add_box(new_box)
        new_box.add_box(existing_box)
    boxes.append(new_box)

print("Making connections")
make_connections(boxes, 1000)

circuits = get_circuits(boxes)
circuits.sort(key=lambda c: c.size(), reverse=True)

print(circuits[0].size() * circuits[1].size() * circuits[2].size())