import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime, Float, Numeric, inspect
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
import hh_db
import datetime

Base = declarative_base()
Session = None

user = 'root'
password = 'secretrootpassword'
host = '11.100.10.100'
port = 3306
database = 'hh_db'

hh_db.initiate_db(user, password, host, port, database)

#USER
userOne = hh_db.User(FirstName='Natalie', LastName='Graser', Email='ngras001@odu.edu', PhoneNumber='571-762-7701',
                                 Password='nataliePassword', IsAtRisk='true', IsVolunteer='false', IsRepresentative='false')
userOneID = hh_db.add_db_object(userOne)
userTwo = hh_db.User(FirstName='Wesley', LastName='Ireland', Email='wes@odu.edu', PhoneNumber='333-444-5555',
                                 Password='wesPassword', IsAtRisk='false', IsVolunteer='false', IsRepresentative='true')
userTwoID = hh_db.add_db_object(userTwo)
userThree = hh_db.User(FirstName='Marissa', LastName='Loya', Email='marissa@odu.edu', PhoneNumber='111-222-3333',
                                 Password='marissaPassword', IsAtRisk='false', IsVolunteer='true', IsRepresentative='false')
userThreeID = hh_db.add_db_object(userThree)
userFour = hh_db.User(FirstName='Wesley', LastName='OSteen', Email='weso@odu.edu', PhoneNumber='222-333-4444',
                                 Password='wesoPassword', IsAtRisk='false', IsVolunteer='false', IsRepresentative='true')
userFourID = hh_db.add_db_object(userFour)
userFive = hh_db.User(FirstName='Alex', LastName='Bonn', Email='alex@odu.edu', PhoneNumber='444-555-6666',
                                 Password='alexPassword', IsAtRisk='false', IsVolunteer='false', IsRepresentative='true')
userFiveID = hh_db.add_db_object(userFive)

#RESOURCE PAGE
resPageOne = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageOneID = hh_db.add_db_object(resPageOne)
resPageTwo = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageTwoID = hh_db.add_db_object(resPageTwo)
resPageThree = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageThreeID = hh_db.add_db_object(resPageThree)
resPageFour = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageFourID = hh_db.add_db_object(resPageFour)
resPageFive = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageFiveID = hh_db.add_db_object(resPageFive)
resPageSix = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageSixID = hh_db.add_db_object(resPageSix)
resPageSeven = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageSevenID = hh_db.add_db_object(resPageSeven)
resPageEight = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageEightID = hh_db.add_db_object(resPageEight)
resPageNine = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageNineID = hh_db.add_db_object(resPageNine)
resPageTen = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageTenID = hh_db.add_db_object(resPageTen)
resPageEleven = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageElevenID = hh_db.add_db_object(resPageEleven)
resPageTwelve = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageTwelveID = hh_db.add_db_object(resPageTwelve)
resPageThirteen = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageThirteenID = hh_db.add_db_object(resPageThirteen)
resPageFourteen = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageFourteenID = hh_db.add_db_object(resPageFourteen)
resPageFifteen = hh_db.RESOURCE_PAGE(LastUpdate=datetime.datetime.now())
resPageFifteenID = hh_db.add_db_object(resPageFifteen)

#ORGANIZATION
orgOne = hh_db.ORGANIZATION(Name='Union Mission Ministries', HQAddress='P.O. Box 3203, Norfolk, VA 23514',
                            PhoneNumber='757-627-8686', Hours='24/7', AcceptingVolunteers='True',
                            VolunteerNotice='Apply Online',
                            HelpSeekerNotice='Call 757-627-8686 to check our availability',
                            Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=1, Legal=0, Veteran=1, Family=1, PageID=resPageOneID)
orgOneID = hh_db.add_db_object(orgOne)
orgTwo = hh_db.ORGANIZATION(Name='The Salvation Army', HQAddress='5525 Raby Rd, Norfolk, Virginia, United States 23502',
                            PhoneNumber='757-543-8100', Hours='24/7', AcceptingVolunteers='True',
                            VolunteerNotice='Apply Online or start a fundraiser',
                            HelpSeekerNotice='Search our locations to get help for yourself or a loved one',
                            Food=1, Shelter=1, Medicine=0, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=1, Legal=0, Veteran=1, Family=0, PageID=resPageTwoID)
orgTwoID = hh_db.add_db_object(orgTwo)

#PROGRAM
progOne = hh_db.PROGRAM(Name='Supplemental Nutrition Assistance Program (SNAP)',
                       Description='Supplemental Nutrition Assistance Program (SNAP) can be used like cash to buy eligible food items from authorized retailers',
                       AcceptingVolunteers=0, VolunteerNotice='',
                            HelpSeekerNotice='', Food=1, Shelter=0, Medicine=0, Clothing=0, Supplies=0, Addiction=0,
                       Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageThreeID)
progOneID = hh_db.add_db_object(progOne)
progTwo = hh_db.PROGRAM(Name='H.O.P.E VILLAGE',
                       Description='We provide stable housing and a 6-month program for qualified applicants who need help getting on their feet.',
                       AcceptingVolunteers=0, VolunteerNotice='Join the Mission or donate online',
                            HelpSeekerNotice='Please note – participants are referred by our Southeastern Virginia Homeless Coalition (SVHC) partner agencies. We cannot accept direct calls for entry into the program. If you are in need of housing assistance, please contact the Regional Housing Crisis Hotline at 757-587-4202. The Regional Crisis Hotline serves as the single point of contact for homeless families and individuals in Hampton Roads.',
                        Food=1, Shelter=1, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                       Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageFourID)
progTwoID = hh_db.add_db_object(progTwo)

#LOCALITY
locOne = hh_db.LOCALITY(Name ='Union Mission Ministries', OrganizationID = orgOneID, ProgramID = None ,
                    Address='5100 E. Virginia Beach Blvd., Norfolk, VA 23502', Latitude='', Longitude='',
                    PhoneNumber='757-627-8686', Hours='24/7', AcceptingVolunteers=1, VolunteerNotice='Apply online',
                    HelpSeekerNotice='Fill out the form online or call us directly at 757-627-8686',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=1, Clothing=1,
                    Supplies=1, Addiction=0,Counseling=1, Legal=0, Veteran=0, Family=1, PageIDPageID=resPageFiveID)
locOneID = hh_db.add_db_object(locOne)
locTwo = hh_db.LOCALITY(Name ='The Hope Center: Mens Shelter', OrganizationID = orgTwoID, ProgramID = None ,
                    Address='203 West 19th Street, Norfolk, VA', Latitude='', Longitude='',
                    PhoneNumber='757-627-8686', Hours='24/7', AcceptingVolunteers=1,
                        VolunteerNotice='Apply online or provide a monetary donation',
                    HelpSeekerNotice='Individuals in need of services, either shelter or day services, '
                                'must have a photo ID. Additionally, potential clients must be sober and drug-free. '
                                     'Day services clients must declare homelessness in order to receive services.',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=0, Clothing=1,
                    Supplies=1, Addiction=0,Counseling=1, Legal=0, Veteran=0, Family=1, PageIDPageID=resPageSixID)
locTwoID = hh_db.add_db_object(locTwo)

#ORG REP
orgRepOne = hh_db.ORG_REPRESENTATIVE(UserID=userTwoID, OrganizationID=orgOneID)
orgRepOneID = hh_db.add_db_object(orgRepOne)

#LOC REP
locRepOne = hh_db.LOC_REPRESENTATIVE(UserID=userFourID, LocalityID=locOneID)
locRepOneID = hh_db.add_db_object(locRepOne)

#PROG REP
progRepOne = hh_db.PROG_REPRESENTATIVE(UserID=userFiveID, ProgramID=progOneID)
progRepOneID = hh_db.add_db_object(progRepOne)

#FORUM
forumOne = hh_db.FORUM(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageOneID)
forumOneID = hh_db.add_db_object(forumOne)

#CLEAN VOTE
cleanOne = hh_db.CLEAN_VOTE(UserID=userOneID, Vote=1, PageID=resPageOneID)
cleanOneID = hh_db.add_db_object(cleanOne)

#RESPONSIVE VOTE
responsiveOne = hh_db.RESPONSIVE_VOTE(UserID=userOneID, Vote=1, PageID=resPageOneID)
responsiveOneID = hh_db.add_db_object(responsiveOne)

#SAFE VOTE
safeOne = hh_db.SAFE_VOTE(UserID=userOneID, Vote=1, PageID=resPageOneID)
safeOneID = hh_db.add_db_object(safeOne)

#USAGE METRICS
metricsOne = hh_db.USAGE_METRICS(PageID=resPageOneID, AvgTimeSpents=5.65,
                                 NumVisits=1, NumForumPosts=1, NumUpVotes=1, NumDownVotes=0)
metricsOneID = hh_db.add_db_object(metricsOne)

#SERVICE
#serviceOne = hh_db.SERVICE(Type='')
#serviceOneID = hh_db.add_db_object(serviceOne)

#ORG SERVICE LINK
#orgServLinkOne = hh_db.ORG_SERVICE_LINK(OrganizationID='', ServiceID='')
#orgServLinkOneID = hh_db.add_db_object(orgServLinkOne)

#LOC SERVICE LINK
#locServLinkOne = hh_db.LOC_SERVICE_LINK(LocalityID='', ServiceID='')
#locServLinkOne = hh_db.add_db_object(locServLinkOne)

#PROG SERVICE LINK
#progServLinkOne = hh_db.PROG_SERVICE_LINK(ProgramID='', ServiceID='')
#progServLinkOneID = hh_db.add_db_object(progServLinkOne)
