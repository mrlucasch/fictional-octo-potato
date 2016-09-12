#!/usr/bin/python


from xml.dom import minidom
import json

xmldoc = minidom.parse('/autograder/source/out.xml')


class TestCase:
    """Represents a node in the xml file"""
    name = ""
    status =""
    time = ""
    classname = ""
    failures = False
    msg = ""
    points = 0
    def __init__(self,name,status,time,classname,points):
        self.name = name
        self.status = status
        self.time = time
        self.classname = classname
        self.points = points
    def Failed(self,msg):
        self.failures = True
        self.msg = msg



class Test:
    """Represents a node in the xml file"""
    tests = 0
    failures = 0
    disabled = 0
    errors = 0
    timestamp = ""
    time =""
    name = ""
    nodes = None
    def __init__(self,tests,failures,disabled,errors,timestamp,time,name,nodes):
        self.tests = tests
        self.failures = failures
        self.disabled = disabled
        self.errors = errors
        self.timestamp = timestamp
        self.time = time
        self.name = name
        self.nodes = nodes



def fetchTestData(node):
    name = node.attributes['name'].value
    status = node.attributes['status'].value
    time = node.attributes['time'].value
    classname = node.attributes['classname'].value
    points = int(node.attributes["Points"].value)
    testdata = TestCase(name,status,time,classname,points)
    if len(node.getElementsByTagName("failure"))!= 0:
        msg = node.getElementsByTagName("failure")[0].attributes['message'].value
        #print msg
        testdata.Failed(msg)
    return testdata



def getTestSuite(xmldoc):
    itemlist = xmldoc.getElementsByTagName('testsuites')
    itemlist = itemlist[0]
    tests = itemlist.attributes['tests'].value
    failures = itemlist.attributes['failures'].value
    disabled = itemlist.attributes['disabled'].value
    errors = itemlist.attributes['errors'].value
    timestamp = itemlist.attributes['timestamp'].value
    time = itemlist.attributes['time'].value
    name = itemlist.attributes['name'].value
    return Test(int(tests),int(failures),int(disabled),int(errors),timestamp,time,name,itemlist.getElementsByTagName('testsuite'))



TS = getTestSuite(xmldoc)



def generateOverallStats(TS):
    total = TS.tests
    total = total- TS.failures
    total = total - TS.disabled
    total = total - TS.errors
    print TS.name+" stats:"
    print "Total Tests: "+str(TS.tests)
    print "Successful:  "+str(total)
    print "Failures:    "+str(TS.failures)
    print "Errors:      "+str(TS.errors)
    print "Disabled:    "+str(TS.disabled)



def gatherData(TS):
    #print TS.nodes[0][0].attributes['name'].value
    tests = []
    for node in TS.nodes:
        for case in node.getElementsByTagName("testcase"):
            tests.append(fetchTestData(case))
    return tests



def calculatePoints(node):
    if node.failures:
        return 0
    else: 
        return node.points



#Takes in test results from gatherData function. Produces list of objects for ouput
def generateJSON(TR):
    final_result = {}
    results_list = []
    for result in TR:
        temp_dict = {}
        temp_dict["name"] = result.name
        temp_dict["score"] = calculatePoints(result)
        temp_dict["max_score"] = result.points
        temp_dict["output"]= result.msg
        results_list.append(temp_dict)
    final_result["tests"]= results_list
    return json.dumps(final_result)


test_results = gatherData(TS)


results = generateJSON(test_results)


print results


