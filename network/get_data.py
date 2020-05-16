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


class Demand:
    def __init__(self, uid, source, destination, demandValue):
        self.uid = uid
        self.source = source
        self.destination = destination
        self.demandValue = demandValue

def get_data(name):
    nodemap = {}

    Read_Data = minidom.parse(name)
    nodelist = Read_Data.getElementsByTagName("node")
    for node in nodelist:
        if node.hasAttribute("id"):
            Nodeid = node.getAttribute("id")
            xCoordinates = node.getElementsByTagName('x')[0].childNodes[0].data
            yCoordinates = node.getElementsByTagName('y')[0].childNodes[0].data
            nodemap[Nodeid] = Node(Nodeid, xCoordinates, yCoordinates)
    del nodelist, node, Nodeid, xCoordinates, yCoordinates

    linklist = Read_Data.getElementsByTagName("link")
    for link in linklist:
        if link.hasAttribute("id"):
            Linkid = link.getAttribute("id")
            Source = link.getElementsByTagName('source')[0].childNodes[0].data
            Destination = link.getElementsByTagName('target')[0].childNodes[0].data
            Capacity = link.getElementsByTagName('capacity')[0].childNodes[0].data
            Cost = link.getElementsByTagName('cost')[0].childNodes[0].data
            linkobj = Link(Linkid, Source, Destination, Capacity, Cost)
            if Source in nodemap:
                nodemap[Source].linklist.append(linkobj)
            else:
                sys.exit('Link error!')

    del linklist, link, Linkid, Source, Destination, Capacity, linkobj

    demandlist = Read_Data.getElementsByTagName("demand")
    for demand in demandlist:
        if demand.hasAttribute("id"):
            Demandid = demand.getAttribute("id")
            Source = demand.getElementsByTagName('source')[0].childNodes[0].data
            Destination = demand.getElementsByTagName('target')[0].childNodes[0].data
            Demandval = demand.getElementsByTagName('demandValue')[0].childNodes[0].data
            demandobj = Demand(Demandid, Source, Destination, Demandval)
            if Source in nodemap:
                nodemap[Source].demandlist.append(demandobj)
            else:
                sys.exit('Demand error!')
    del demandlist, demand, Demandid, Source, Destination, Demandval, demandobj
    del Read_Data

    return nodemap
