import sys

from xml.dom import minidom


class Node:
    def __init__(self, uid, x, y):
        self.uid = uid
        self.x = x
        self.y = y
        self.linklist = []
        self.demandlist = []


class Link:
    def __init__(self, uid, source, target, capacity, cost):
        self.uid = uid
        self.source = source
        self.target = target
        self.capacity = capacity
        self.cost = cost
        self.pheromone = 0
        self.occupancy = 0


class Demand:
    def __init__(self, uid, source, destination, demandValue):
        self.uid = uid
        self.source = source
        self.destination = destination
        self.demandValue = demandValue


def get_data(filename):
    Read_Data = minidom.parse(filename)

    nodemap = _get_NodeList(Read_Data)
    linklist = _get_Linklist(Read_Data, nodemap)
    demandlist = _get_Demandlist(Read_Data, nodemap)

    return nodemap, linklist, demandlist


def _get_NodeList(read_data):
    nodemap = {}

    nodelist = read_data.getElementsByTagName("node")
    for node in nodelist:
        if node.hasAttribute("id"):
            Nodeid = node.getAttribute("id")
            xCoordinates = node.getElementsByTagName('x')[0].childNodes[0].data
            yCoordinates = node.getElementsByTagName('y')[0].childNodes[0].data
            nodemap[Nodeid] = Node(Nodeid, float(xCoordinates), float(yCoordinates))

    return nodemap


def _get_Linklist(read_data, nodemap):
    links = {}

    linklist = read_data.getElementsByTagName("link")
    for link in linklist:
        if link.hasAttribute("id"):
            Linkid = link.getAttribute("id")
            Source = link.getElementsByTagName('source')[0].childNodes[0].data
            Destination = link.getElementsByTagName('target')[0].childNodes[0].data
            Capacity = link.getElementsByTagName('capacity')[0].childNodes[0].data
            Cost = link.getElementsByTagName('cost')[0].childNodes[0].data
            linkobj = Link(Linkid, Source, Destination, int(float(Capacity)), int(float(Cost)))
            if Source in nodemap:
                nodemap[Source].linklist.append(linkobj)
            else:
                sys.exit('Link error!')
            links[linkobj.uid] = linkobj

    return links


def _get_Demandlist(read_data, nodemap):
    demands = {}

    demandlist = read_data.getElementsByTagName("demand")
    for demand in demandlist:
        if demand.hasAttribute("id"):
            Demandid = demand.getAttribute("id")
            Source = demand.getElementsByTagName('source')[0].childNodes[0].data
            Destination = demand.getElementsByTagName('target')[0].childNodes[0].data
            Demandval = demand.getElementsByTagName('demandValue')[0].childNodes[0].data
            demandobj = Demand(Demandid, Source, Destination, int(float(Demandval)))
            if Source in nodemap:
                nodemap[Source].demandlist.append(demandobj)
            else:
                sys.exit('Demand error!')
            demands[demandobj.uid] = demandobj

    return demands
