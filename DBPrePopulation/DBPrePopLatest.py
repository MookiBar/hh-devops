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
password = 'password123'
host = '127.0.0.1'
port = 3306
database = 'HH'

hh_db.initiate_db(user, password, host, port, database)

#USER
userOne = hh_db.User(FirstName='Natalie', LastName='Graser', Email='ngras001@odu.edu', PhoneNumber='571-762-7701',
                                 Password='nataliePassword', IsAtRisk=True, IsVolunteer=False, IsRepresentative=False)
userOneID = hh_db.add_db_object(userOne)
userTwo = hh_db.User(FirstName='Wesley', LastName='Ireland', Email='wes@odu.edu', PhoneNumber='333-444-5555',
                                 Password='wesPassword', IsAtRisk=False, IsVolunteer=False, IsRepresentative=True)
userTwoID = hh_db.add_db_object(userTwo)
userThree = hh_db.User(FirstName='Marissa', LastName='Loya', Email='marissa@odu.edu', PhoneNumber='111-222-3333',
                                 Password='marissaPassword', IsAtRisk=False, IsVolunteer=True, IsRepresentative=False)
userThreeID = hh_db.add_db_object(userThree)
userFour = hh_db.User(FirstName='Wesley', LastName='OSteen', Email='weso@odu.edu', PhoneNumber='222-333-4444',
                                 Password='wesoPassword', IsAtRisk=False, IsVolunteer=False, IsRepresentative=True)
userFourID = hh_db.add_db_object(userFour)
userFive = hh_db.User(FirstName='Alex', LastName='Bonn', Email='alex@odu.edu', PhoneNumber='444-555-6666',
                                 Password='alexPassword', IsAtRisk=False, IsVolunteer=False, IsRepresentative=True)
userFiveID = hh_db.add_db_object(userFive)
userSix = hh_db.User(FirstName='Kenny', LastName='Dang', Email='kenny@odu.edu', PhoneNumber='555-666-7777',
                                 Password='kennyPassword', IsAtRisk=True, IsVolunteer=False, IsRepresentative=False)
userSixID = hh_db.add_db_object(userSix)
userSeven = hh_db.User(FirstName='Harry', LastName='Potter', Email='yerawizard@odu.edu', PhoneNumber='555-666-7777',
                                 Password='potterPassword', IsAtRisk=False, IsVolunteer=True, IsRepresentative=False)
userSevenID = hh_db.add_db_object(userSeven)
userEight = hh_db.User(FirstName='Severus', LastName='Snape', Email='profsnape@odu.edu', PhoneNumber='666-777-8888',
                                 Password='snapePassword', IsAtRisk=False, IsVolunteer=False, IsRepresentative=True)
userEightID = hh_db.add_db_object(userEight)
userNine = hh_db.User(FirstName='Albus', LastName='Dumbledore', Email='dumbledore@odu.edu', PhoneNumber='888-999-0000',
                                 Password='dumbledorePassword', IsAtRisk=False, IsVolunteer=False, IsRepresentative=True)
userNineID = hh_db.add_db_object(userNine)
userTen = hh_db.User(FirstName='Minerva', LastName='McGonagall', Email='gryffindor@odu.edu', PhoneNumber='777-666-5555',
                                 Password='potterPassword', IsAtRisk=False, IsVolunteer=False, IsRepresentative=True)
userTenID = hh_db.add_db_object(userTen)

#RESOURCE PAGE
resPageOne = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageOneID = hh_db.add_db_object(resPageOne)
resPageTwo = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageTwoID = hh_db.add_db_object(resPageTwo)
resPageThree = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageThreeID = hh_db.add_db_object(resPageThree)
resPageFour = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageFourID = hh_db.add_db_object(resPageFour)
resPageFive = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageFiveID = hh_db.add_db_object(resPageFive)
resPageSix = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageSixID = hh_db.add_db_object(resPageSix)
resPageSeven = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageSevenID = hh_db.add_db_object(resPageSeven)
resPageEight = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageEightID = hh_db.add_db_object(resPageEight)
resPageNine = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageNineID = hh_db.add_db_object(resPageNine)
resPageTen = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageTenID = hh_db.add_db_object(resPageTen)
resPageEleven = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageElevenID = hh_db.add_db_object(resPageEleven)
resPageTwelve = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageTwelveID = hh_db.add_db_object(resPageTwelve)
resPageThirteen = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageThirteenID = hh_db.add_db_object(resPageThirteen)
resPageFourteen = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageFourteenID = hh_db.add_db_object(resPageFourteen)
resPageFifteen = hh_db.Resource_Page(LastUpdate=datetime.datetime.now())
resPageFifteenID = hh_db.add_db_object(resPageFifteen)

#Organization
orgOne = hh_db.Organization(Name='Union Mission Ministries', HQAddress='P.O. Box 3203, Norfolk, VA 23514',
                            PhoneNumber='757-627-8686', Hours='24/7', AcceptingVolunteers=True,
                            VolunteerNotice='Apply Online',
                            HelpSeekerNotice='Call 757-627-8686 to check our availability',
                            Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=1, Legal=0, Veteran=1, Family=1, PageID=resPageOneID)
orgOneID = hh_db.add_db_object(orgOne)
orgTwo = hh_db.Organization(Name='The Salvation Army', HQAddress='5525 Raby Rd, Norfolk, Virginia, United States 23502',
                            PhoneNumber='757-543-8100', Hours='24/7', AcceptingVolunteers=True,
                            VolunteerNotice='Apply Online or start a fundraiser',
                            HelpSeekerNotice='Search our locations to get help for yourself or a loved one',
                            Food=1, Shelter=1, Medicine=0, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=1, Legal=0, Veteran=1, Family=0, PageID=resPageTwoID)
orgTwoID = hh_db.add_db_object(orgTwo)
orgThree = hh_db.Organization(Name='H.O.P.E. Foundation', HQAddress='2085 Lynnhaven Parkway Suite 106, Box 128, Virginia Beach, VA 23456',
                            PhoneNumber='757-241-6900', Hours='24/7', AcceptingVolunteers=True,
                            VolunteerNotice='Please fill out the form online for more information.',
                            HelpSeekerNotice='Please fill out the form online for more information.',
                            Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=1,
                            Counseling=1, Legal=1, Veteran=1, Family=1, PageID=resPageEightID)
orgThreeID = hh_db.add_db_object(orgThree)

#Program
progOne = hh_db.Program(Name='Supplemental Nutrition Assistance Program (SNAP)',
                       Description='Supplemental Nutrition Assistance Program (SNAP) can be used like cash to buy eligible food items from authorized retailers',
                       AcceptingVolunteers=0, VolunteerNotice='',
                            HelpSeekerNotice='', Food=1, Shelter=0, Medicine=0, Clothing=0, Supplies=0, Addiction=0,
                       Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageThreeID)
progOneID = hh_db.add_db_object(progOne)
progTwo = hh_db.Program(Name='H.O.P.E VILLAGE',
                       Description='We provide stable housing and a 6-month program for qualified applicants who need help getting on their feet.',
                       AcceptingVolunteers=0, VolunteerNotice='Join the Mission or donate online',
                            HelpSeekerNotice='Please note – participants are referred by our Southeastern Virginia Homeless Coalition (SVHC) partner agencies. We cannot accept direct calls for entry into the program. If you are in need of housing assistance, please contact the Regional Housing Crisis Hotline at 757-587-4202. The Regional Crisis Hotline serves as the single point of contact for homeless families and individuals in Hampton Roads.',
                        Food=1, Shelter=1, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                       Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageFourID)
progTwoID = hh_db.add_db_object(progTwo)
progThree = hh_db.Program(Name='H.O.P.E on Wheels',
                       Description='We launch H.O.P.E. on Wheels every May to ensure we are able to provide the community with food and resources to help them through difficult times.',
                       AcceptingVolunteers=1, VolunteerNotice='Use our online form to donate or volunteer.',
                            HelpSeekerNotice='Use our online form to find out more information. If you are in need of shelter call Crisis Hotline: 757-587-4202',
                        Food=1, Shelter=0, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                       Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageNineID)
progThreeID = hh_db.add_db_object(progThree)

#Locality
locOne = hh_db.Locality(Name ='Union Mission Ministries', OrganizationID = orgOneID, ProgramID = None ,
                    Address='5100 E. Virginia Beach Blvd., Norfolk, VA 23502', Latitude='36.84458', Longitude='-76.15324',
                    PhoneNumber='757-627-8686', Hours='24/7', AcceptingVolunteers=1, VolunteerNotice='Apply online',
                    HelpSeekerNotice='Fill out the form online or call us directly at 757-627-8686',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=1, Clothing=1,
                    Supplies=1, Addiction=0,Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageFiveID)
locOneID = hh_db.add_db_object(locOne)
locTwo = hh_db.Locality(Name ='The Hope Center: Mens Shelter', OrganizationID = orgTwoID, ProgramID = None ,
                    Address='203 West 19th Street, Norfolk, VA', Latitude='36.86696', Longitude='-76.28707',
                    PhoneNumber='757-627-8686', Hours='24/7', AcceptingVolunteers=1,
                        VolunteerNotice='Apply online or provide a monetary donation',
                    HelpSeekerNotice='Individuals in need of services, either shelter or day services, '
                                'must have a photo ID. Additionally, potential clients must be sober and drug-free. '
                                     'Day services clients must declare homelessness in order to receive services.',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=0, Clothing=1,
                    Supplies=1, Addiction=0,Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageSixID)
locTwoID = hh_db.add_db_object(locTwo)
locThree = hh_db.Locality(Name ='Salvation Army Food Pantry', OrganizationID = orgTwoID, ProgramID = None ,
                    Address='5525 Raby Road, Norfolk, VA', Latitude='36.85696', Longitude='-76.21823',
                    PhoneNumber='757-965-9012', Hours='M-Th 1-3:3pm, F 1-2pm', AcceptingVolunteers=0,
                        VolunteerNotice='',
                    HelpSeekerNotice='For more information, please call 757-965-9012 Option 2.',
                        ProvidesTransportation=0, Food=1, Shelter=0, Medicine=0, Clothing=0,
                    Supplies=0, Addiction=0,Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageSevenID)
locThreeID = hh_db.add_db_object(locThree)
locFour = hh_db.Locality(Name ='H.O.P.E. Shelter', OrganizationID = orgThreeID, ProgramID = progThreeID ,
                    Address='434 St. Paul’s Blvd. Norfolk, VA', Latitude='36.85095', Longitude='-76.28408',
                    PhoneNumber='757-241-6900', Hours='Sun, Wed, Fri 5pm to 7 pm', AcceptingVolunteers=1,
                        VolunteerNotice='Please use the online form to learn how to donate or volunteer.',
                    HelpSeekerNotice='For more information or resources contact us by Phone:(757-241-6900) or Email– hopefoundationinc@cox.net',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=1,
                            Counseling=1, Legal=1, Veteran=1, Family=1, PageID=resPageTenID)
locFourID = hh_db.add_db_object(locFour)

#ORG REP
orgRepOne = hh_db.Org_Representative(UserID=userTwoID, OrganizationID=orgOneID)
orgRepOneID = hh_db.add_db_object(orgRepOne)

#LOC REP
locRepOne = hh_db.Loc_Representative(UserID=userFourID, LocalityID=locOneID)
locRepOneID = hh_db.add_db_object(locRepOne)

#PROG REP
progRepOne = hh_db.Prog_Representative(UserID=userFiveID, ProgramID=progOneID)
progRepOneID = hh_db.add_db_object(progRepOne)

#Forum
forumOne = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageOneID)
forumOneID = hh_db.add_db_object(forumOne)

#CLEAN VOTE
cleanOne = hh_db.Clean_Vote(UserID=userOneID, Vote=1, PageID=resPageOneID)
cleanOneID = hh_db.add_db_object(cleanOne)
cleanTwo = hh_db.Clean_Vote(UserID=userThreeID, Vote=0, PageID=resPageOneID)
cleanTwoID = hh_db.add_db_object(cleanTwo)
cleanThree = hh_db.Clean_Vote(UserID=userFiveID, Vote=1, PageID=resPageOneID)
cleanThreeID = hh_db.add_db_object(cleanThree)
cleanFour = hh_db.Clean_Vote(UserID=userFourID, Vote=0, PageID=resPageTwoID)
cleanFourID = hh_db.add_db_object(cleanFour)
cleanFive = hh_db.Clean_Vote(UserID=userTwoID, Vote=1, PageID=resPageTwoID)
cleanFiveID = hh_db.add_db_object(cleanFive)

#RESPONSIVE VOTE
responsiveOne = hh_db.Responsive_Vote(UserID=userOneID, Vote=1, PageID=resPageOneID)
responsiveOneID = hh_db.add_db_object(responsiveOne)
responsiveTwo = hh_db.Responsive_Vote(UserID=userThreeID, Vote=0, PageID=resPageOneID)
responsiveTwoID = hh_db.add_db_object(responsiveTwo)
responsiveThree = hh_db.Responsive_Vote(UserID=userFiveID, Vote=1, PageID=resPageOneID)
responsiveThreeID = hh_db.add_db_object(responsiveThree)
responsiveFour = hh_db.Responsive_Vote(UserID=userOneID, Vote=1, PageID=resPageTwoID)
responsiveFourID = hh_db.add_db_object(responsiveFour)
responsiveFive = hh_db.Responsive_Vote(UserID=userThreeID, Vote=0, PageID=resPageTwoID)
responsiveFiveID = hh_db.add_db_object(responsiveFive)
responsiveSix = hh_db.Responsive_Vote(UserID=userFiveID, Vote=0, PageID=resPageTwoID)
responsiveSixID = hh_db.add_db_object(responsiveSix)


#SAFE VOTE
safeOne = hh_db.Safe_Vote(UserID=userOneID, Vote=1, PageID=resPageOneID)
safeOneID = hh_db.add_db_object(safeOne)
safeTwo = hh_db.Safe_Vote(UserID=userTwoID, Vote=0, PageID=resPageOneID)
safeTwoID = hh_db.add_db_object(safeTwo)
safeThree = hh_db.Safe_Vote(UserID=userThreeID, Vote=1, PageID=resPageOneID)
safeThreeID = hh_db.add_db_object(safeThree)
safeFour = hh_db.Safe_Vote(UserID=userFourID, Vote=0, PageID=resPageOneID)
safeFourID = hh_db.add_db_object(safeFour)
safeFive = hh_db.Safe_Vote(UserID=userFiveID, Vote=1, PageID=resPageOneID)
safeFiveID = hh_db.add_db_object(safeFive)
safeSix = hh_db.Safe_Vote(UserID=userOneID, Vote=0, PageID=resPageTwoID)
safeSixID = hh_db.add_db_object(safeSix)
safeSeven = hh_db.Safe_Vote(UserID=userTwoID, Vote=1, PageID=resPageTwoID)
safeSevenID = hh_db.add_db_object(safeSeven)

#USAGE METRICS
#metricsOne = hh_db.Usage_Metrics(PageID=resPageOneID, AvgTimeSpent=5.65,
#                                 NumVisitsAtRisk=1, NumVisitsVolunteer=1, NumVisitsRepresentative=1,
#                                 NumVisitsOther=1, NumForumPosts=1, NumUpVotesClean=1, NumDownVotesClean=0,
#                                 NumUpVotesResponsive=1, NumDownVotesResponsive=0, NumUpVotesSafe=1, NumDownVotesSafe=0)
#metricsOneID = hh_db.add_db_object(metricsOne)

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
