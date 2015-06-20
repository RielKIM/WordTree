# WordTree

##Introduction
------------
WordTree is splunk visualization app for analyzing a lot of sentences. 
This app is using google chart api.
If you want to read about google word tree chart, refer the following URL.
https://developers.google.com/chart/interactive/docs/gallery/wordtree

##Installation
------------
1. Download splunk enterprise. (Refer http://www.splunk.com/en_us/download/splunk-enterprise.html)
2. git clone to $SPLUNK_HOME$/etc/apps/
3. Start splunk start

##Usage
-----
This app is providing two ways for getting contents which will be analyzed.
First one is copy & paste the other one is querying to splunk.
If you want to use copy & paste, you should set options which is on top of page then paste contents in text box on bottom of page.
When you use way to query to splunk, you should set options and make query.
When you write query, you should change target column name as ‘Data’.
