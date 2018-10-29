#########################################
#    Exponential Random Graph Model     #
#           Example Problem             #
#           Gray's Anatomy              #
#                                       #
#   Data: Garry Weissman, 2011          #
#                                       #
#########################################
rm(list=ls())
library("statnet")


# Load Data: Requires data sets 'facebook-adj.csv' & 'facebook-attr.csv'
ga.matrix<-as.matrix(read.table("/Users/mirandamyers/git/social-media-analytics/projects/network-statistical-analysis/facebook-adj.csv", #the name of the adjacency matrix
                                sep=",", #the spreadsheet uses commas to separate cells
                                header=T, #because there is a header with node ID
                                row.names=1, #because the first column has node ID
                                quote="\""))

ga.attr<-read.csv("/Users/mirandamyers/git/social-media-analytics/projects/network-statistical-analysis/facebook-attr.csv",  #the name of the attributes file
                  header=TRUE, 
                  sep=",", 
                  stringsAsFactors = FALSE)

#Convert the data into a network object in statnet
ga.net<-network(ga.matrix, 
                vertex.attr = ga.attr,
                vertex.attrnames = colnames(ga.attr),
                directed=F, 
                loops=F, 
                multiple=F, 
                bipartite=F, 
                hyper=F)

# Plot the network
plot(ga.net, 
     vertex.col=c("blue","pink")[1+(get.vertex.attribute(ga.net, "gender77")=="1")],
     label=get.vertex.attribute(ga.net, "vertex.names"), 
     label.cex=.7)

# Conduct Exponential Random Graph Models (ERGM) Analysis

#Restricted
e2<-ergm(ga.net~edges)  #Create a restricted model with just edges term
summary(e2)

e3<-ergm(ga.net~edges+triangle)  #include a triadic effect in the model
summary(e3)

e6<-ergm(ga.net~triangle)  #include a triadic effect in the model
summary(e6)

#Unrestricted
e4<-ergm(ga.net~edges+nodematch("gender77"))  #Create an unrestricted model
summary(e4)

e5<-ergm(ga.net~edges+nodematch("educationtype53"))  #Testing a racial homophily hypothesis
summary(e5)

e12<-ergm(ga.net~edges+gwesp(0.5))  #Testing gwesp
summary(e12)

# Not covered: goodness of fit testing and dealing with degenerate models

