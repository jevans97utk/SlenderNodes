## DataONE SlenderNode Connectors

[DataONE](dataone.org) has coined the term "SlenderNode" to refer to a design pattern that allows 3rd party repositories to become DataONE [Member Nodes](https://www.dataone.org/current-member-nodes#uploads) without having to go through the time consuming task of implementing complete custom Member Nodes. 

Instead, one of DataONE's existing Member Nodes, currently [Metacat](https://www.dataone.org/software-tools/metacat) or the [Generic Member Node (GMN)](http://pythonhosted.org/dataone.generic_member_node/), is used as a front end for the native repository by adding a software component called a SlenderNode Connector.

The connector pulls data from the native repository and creates corresponding data objects in the front end Member Node. In the process, the data is often transformed in various ways or has metadata added to it in order to make the data more convenient for end users to consume through DataONE. E.g., a single object in the native repository may become multiple objects in DataONE.

This repository contains SlenderNode Connectors that have been implemented directly by DataONE.
