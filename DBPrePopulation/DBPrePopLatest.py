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
                            PhoneNumber='757-627-8686', Hours='24/7', WebsiteLink='http://www.unionmissionministries.org/',
			                ImageURL='http://www.unionmissionministries.org/wp-content/uploads/2015/09/logo.png',
			                AcceptingVolunteers=True, VolunteerNotice='Apply Online',
                            HelpSeekerNotice='Call 757-627-8686 to check our availability',
                            Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=1, Legal=0, Veteran=1, Family=1, PageID=resPageOneID)
orgOneID = hh_db.add_db_object(orgOne)
orgTwo = hh_db.Organization(Name='The Salvation Army', HQAddress='5525 Raby Rd, Norfolk, Virginia, United States 23502',
                            PhoneNumber='757-543-8100', Hours='24/7', WebsiteLink='https://salvationarmypotomac.org/',
			                ImageURL='https://salvationarmypotomac.org/wp-content/uploads/2021/01/DTMG-Logo-2-Lines_Potomac-1.jpg',
			                AcceptingVolunteers=True, VolunteerNotice='Apply Online or start a fundraiser',
                            HelpSeekerNotice='Search our locations to get help for yourself or a loved one',
                            Food=1, Shelter=1, Medicine=0, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=1, Legal=0, Veteran=1, Family=0, PageID=resPageTwoID)
orgTwoID = hh_db.add_db_object(orgTwo)
orgThree = hh_db.Organization(Name='H.O.P.E. Foundation', HQAddress='2085 Lynnhaven Parkway Suite 106, Box 128, Virginia Beach, VA 23456',
                            PhoneNumber='757-241-6900', Hours='24/7', WebsiteLink='https://hopefdn.org/',
			                ImageURL='https://hopefdn.org/wp-content/uploads/elementor/thumbs/cropped-H.O.P.E-Foundation-Inc.-Logo-ppsqq0p4pwc0ll4d3lckpsnr4xtac4ocbfx9vreb14.png',
			                AcceptingVolunteers=True, VolunteerNotice='Please fill out the form online for more information.',
                            HelpSeekerNotice='Please fill out the form online for more information.',
                            Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=1,
                            Counseling=1, Legal=1, Veteran=1, Family=1, PageID=resPageEightID)
orgThreeID = hh_db.add_db_object(orgThree)
orgFour = hh_db.Organization(Name='Norfolk Urban Outreach Ministry', HQAddress='972 Norfolk Square, Norfolk, VA',
                            PhoneNumber=' 757-461-4213', Hours='Mon-Fri 9AM-3PM', WebsiteLink='https://nuom.org/',
			                ImageURL='https://nuom.org/wp-content/uploads/2018/07/nuom-logo-white-200.png',
			                AcceptingVolunteers=False, VolunteerNotice='Please fill out the form online for more information or make a donation.',
                            HelpSeekerNotice='Please fill out the form online for more information or call us.',
                            Food=1, Shelter=1, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                            Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageElevenID)
orgFourID = hh_db.add_db_object(orgFour)
orgFive = hh_db.Organization(Name='PiN Ministry', HQAddress='1164 Miller’s Lane Suite A, Virginia Beach, VA 23451',
                            PhoneNumber='757-962-3567', Hours='Mon-Sat 9AM-5PM', WebsiteLink='https://pinministry.org/',
			                ImageURL='https://q135eb.p3cdn1.secureserver.net/wp-content/uploads/2022/05/header-lrg.png',
			                AcceptingVolunteers=True, VolunteerNotice='Sign up to volunteer or donate online.',
                            HelpSeekerNotice='To learn more about our emergency and recovery services, please call us at (757) 962-3567 or send us a message.',
                            Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=0,
                            Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageThirteenID)
orgFiveID = hh_db.add_db_object(orgFive)

#Program
progOne = hh_db.Program(Name='Supplemental Nutrition Assistance Program (SNAP)',
                        Description='Supplemental Nutrition Assistance Program (SNAP) can be used like cash to buy eligible food items from authorized retailers',
                        WebsiteLink='https://www.fns.usda.gov/snap/supplemental-nutrition-assistance-program', ImageURL='https://www.fns.usda.gov/themes/custom/fns_uswds/assets/img/usda/usda-logo-color.svg',
                        AcceptingVolunteers=0, VolunteerNotice='',
                        HelpSeekerNotice='', Food=1, Shelter=0, Medicine=0, Clothing=0, Supplies=0, Addiction=0,
                        Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageThreeID)
progOneID = hh_db.add_db_object(progOne)
progTwo = hh_db.Program(Name='H.O.P.E VILLAGE',
                        Description='We provide stable housing and a 6-month program for qualified applicants who need help getting on their feet.',
                        WebsiteLink='https://salvationarmypotomac.org/hrva/programs/residentialhousing/', ImageURL='https://salvationarmypotomac.org/hrva/files/2021/07/Hope-Village-Banner.png',
                        AcceptingVolunteers=0, VolunteerNotice='Join the Mission or donate online',
                        HelpSeekerNotice='Please note – participants are referred by our Southeastern Virginia Homeless Coalition (SVHC) partner agencies. We cannot accept direct calls for entry into the program. If you are in need of housing assistance, please contact the Regional Housing Crisis Hotline at 757-587-4202. The Regional Crisis Hotline serves as the single point of contact for homeless families and individuals in Hampton Roads.',
                        Food=1, Shelter=1, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                        Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageFourID)
progTwoID = hh_db.add_db_object(progTwo)
progThree = hh_db.Program(Name='H.O.P.E on Wheels',
                        Description='We launch H.O.P.E. on Wheels every May to ensure we are able to provide the community with food and resources to help them through difficult times.',
                        WebsiteLink='https://www.hamptonroadsendshomelessness.org/get-help.html', ImageURL='https://www.hamptonroadsendshomelessness.org/uploads/5/2/5/7/52579065/hch_orig.png',
                        AcceptingVolunteers=1, VolunteerNotice='Use our online form to donate or volunteer.',
                        HelpSeekerNotice='Use our online form to find out more information. If you are in need of shelter call Crisis Hotline: 757-587-4202',
                        Food=1, Shelter=0, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                        Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageNineID)
progThreeID = hh_db.add_db_object(progThree)
progFour = hh_db.Program(Name='H20 Water Assistance',
                        Description='Eligible clients can receive up to $500 in program assistance toward eligible account costs once in any twelve-month period.',
                        WebsiteLink='https://salvationarmypotomac.org/hrva/programs/h20-water-assistance/', ImageURL='https://salvationarmypotomac.org/hrva/files/2022/08/ShareH2OLogos-01-1030x624.png',
                        AcceptingVolunteers=0, VolunteerNotice='Donate online to assist a local family in your neighborhood.',
                        HelpSeekerNotice='Contact the Regional Housing Crisis Hotline (757-227-5932) for H2O referral',
                        Food=0, Shelter=0, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                        Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageTwelveID)
progFourID = hh_db.add_db_object(progFour)
progFive = hh_db.Program(Name='Heating & Cooling Assistance',
                        Description='Program funds are used to stop disconnection or to reconnect primary heating or cooling source.',
                        WebsiteLink='https://salvationarmypotomac.org/hrva/programs/utility-assistance/', ImageURL='https://salvationarmypotomac.org/hrva/files/2021/02/HRVALogo.jpg',
                        AcceptingVolunteers=0, VolunteerNotice='Check the EnergyShare box on your utility bill and make a donation.',
                        HelpSeekerNotice='Clients must call the EnergyShare hotline, 757-965-9012 ext. 1 to obtain all current information',
                        Food=0, Shelter=0, Medicine=0, Clothing=0, Supplies=1, Addiction=0,
                        Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageFifteenID)
progFiveID = hh_db.add_db_object(progFive)

#Locality
locOne = hh_db.Locality(Name ='Union Mission Ministries', OrganizationID = orgOneID, ProgramID = None ,
                        Address='5100 E. Virginia Beach Blvd., Norfolk, VA 23502', Latitude='36.84458', Longitude='-76.15324',
                        PhoneNumber='757-627-8686', Hours='24/7',
                        WebsiteLink='http://www.unionmissionministries.org/', ImageURL='http://www.unionmissionministries.org/wp-content/uploads/2015/09/logo.png',
                        AcceptingVolunteers=1, VolunteerNotice='Apply online',
                        HelpSeekerNotice='Fill out the form online or call us directly at 757-627-8686',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=1, Clothing=1,
                        Supplies=1, Addiction=0,Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageFiveID)
locOneID = hh_db.add_db_object(locOne)
locTwo = hh_db.Locality(Name ='The Hope Center: Mens Shelter', OrganizationID = orgTwoID, ProgramID = None ,
                        Address='203 West 19th Street, Norfolk, VA', Latitude='36.86696', Longitude='-76.28707',
                        PhoneNumber='757-627-8686', Hours='24/7',
                        WebsiteLink='https://salvationarmypotomac.org/hrva/programs/mens-shelter/', ImageURL='https://salvationarmypotomac.org/wp-content/uploads/2021/01/DTMG-Logo-2-Lines_Potomac-1.jpg',
                        AcceptingVolunteers=1, VolunteerNotice='Apply online or provide a monetary donation',
                        HelpSeekerNotice='Individuals in need of services, either shelter or day services, '
                                'must have a photo ID. Additionally, potential clients must be sober and drug-free. '
                                     'Day services clients must declare homelessness in order to receive services.',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=0, Clothing=1,
                        Supplies=1, Addiction=0,Counseling=1, Legal=0, Veteran=0, Family=1, PageID=resPageSixID)
locTwoID = hh_db.add_db_object(locTwo)
locThree = hh_db.Locality(Name ='Salvation Army Food Pantry', OrganizationID = orgTwoID, ProgramID = None ,
                        Address='5525 Raby Road, Norfolk, VA', Latitude='36.85696', Longitude='-76.21823',
                        PhoneNumber='757-965-9012', Hours='M-Th 1-3:3pm, F 1-2pm',
                        WebsiteLink='https://www.salvationarmyusa.org/usn/cure-hunger/', ImageURL='https://salvationarmypotomac.org/wp-content/uploads/2021/01/DTMG-Logo-2-Lines_Potomac-1.jpg',
                        AcceptingVolunteers=0, VolunteerNotice='',
                        HelpSeekerNotice='For more information, please call 757-965-9012 Option 2.',
                        ProvidesTransportation=0, Food=1, Shelter=0, Medicine=0, Clothing=0,
                        Supplies=0, Addiction=0,Counseling=0, Legal=0, Veteran=0, Family=1, PageID=resPageSevenID)
locThreeID = hh_db.add_db_object(locThree)
locFour = hh_db.Locality(Name ='H.O.P.E. Shelter', OrganizationID = orgThreeID, ProgramID = progThreeID ,
                        Address='434 St. Paul’s Blvd. Norfolk, VA', Latitude='36.85095', Longitude='-76.28408',
                        PhoneNumber='757-241-6900', Hours='Sun, Wed, Fri 5pm to 7 pm',
                        WebsiteLink='https://salvationarmypotomac.org/hrva/programs/residentialhousing/', ImageURL='https://salvationarmypotomac.org/hrva/files/2021/07/Hope-Village-Banner.png',
                        AcceptingVolunteers=1, VolunteerNotice='Please use the online form to learn how to donate or volunteer.',
                        HelpSeekerNotice='For more information or resources contact us by Phone:(757-241-6900) or Email– hopefoundationinc@cox.net',
                        ProvidesTransportation=0, Food=1, Shelter=1, Medicine=1, Clothing=1, Supplies=1, Addiction=1,
                        Counseling=1, Legal=1, Veteran=1, Family=1, PageID=resPageTenID)
locFourID = hh_db.add_db_object(locFour)
locFive = hh_db.Locality(Name ='PiN Essential Services', OrganizationID = orgFiveID, ProgramID = None,
                        Address='1164 Miller’s Lane Suite A, Virginia Beach, VA 23451', Latitude='36.83894', Longitude='-76.00019',
                        PhoneNumber='757-962-3567', Hours='M-Th 1-4pm, Sat 11am-2pm',
                        WebsiteLink='https://pinministry.org/', ImageURL='https://q135eb.p3cdn1.secureserver.net/wp-content/uploads/2022/05/header-lrg.png',
                        AcceptingVolunteers=1, VolunteerNotice='Please sign up online to volunteer.',
                        HelpSeekerNotice='If you are currently living outside, you may come in for 3 hours during service hours.',
                        ProvidesTransportation=0, Food=0, Shelter=0, Medicine=1, Clothing=1, Supplies=1, Addiction=0,
                        Counseling=0, Legal=0, Veteran=0, Family=0, PageID=resPageFourteenID)
locFiveID = hh_db.add_db_object(locFive)

#ORG REP
orgRepOne = hh_db.Org_Representative(UserID=userTwoID, OrganizationID=orgOneID)
orgRepOneID = hh_db.add_db_object(orgRepOne)
orgRepTwo = hh_db.Org_Representative(UserID=userEightID, OrganizationID=orgTwoID)
orgRepTwoID = hh_db.add_db_object(orgRepTwo)

#LOC REP
locRepOne = hh_db.Loc_Representative(UserID=userFourID, LocalityID=locOneID)
locRepOneID = hh_db.add_db_object(locRepOne)
locRepTwo = hh_db.Loc_Representative(UserID=userNineID, LocalityID=locTwoID)
locRepTwoID = hh_db.add_db_object(locRepTwo)

#PROG REP
progRepOne = hh_db.Prog_Representative(UserID=userFiveID, ProgramID=progOneID)
progRepOneID = hh_db.add_db_object(progRepOne)
progRepTwo = hh_db.Prog_Representative(UserID=userTenID, ProgramID=progTwoID)
progRepTwoID = hh_db.add_db_object(progRepTwo)

#Forum
forumOne = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageOneID)
forumOneID = hh_db.add_db_object(forumOne)
forumTwo = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageTwoID)
forumTwoID = hh_db.add_db_object(forumTwo)
forumThree = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageThreeID)
forumThreeID = hh_db.add_db_object(forumThree)
forumFour = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageFourID)
forumFourID = hh_db.add_db_object(forumFour)
forumFive = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageFiveID)
forumFiveID = hh_db.add_db_object(forumFive)
forumSix = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageSixID)
forumSixID = hh_db.add_db_object(forumSix)
forumSeven = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageSevenID)
forumSevenID = hh_db.add_db_object(forumSeven)
forumEight = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageEightID)
forumEightID = hh_db.add_db_object(forumEight)
forumNine = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageNineID)
forumNineID = hh_db.add_db_object(forumNine)
forumTen = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageTenID)
forumTenID = hh_db.add_db_object(forumTen)
forumEleven = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageElevenID)
forumElevenID = hh_db.add_db_object(forumEleven)
forumTwelve = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageTwelveID)
forumTwelveID = hh_db.add_db_object(forumTwelve)
forumThirteen = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageThirteenID)
forumThirteenID = hh_db.add_db_object(forumThirteen)
forumFourteen = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageFourteenID)
forumFourteenID = hh_db.add_db_object(forumFourteen)
forumFifteen = hh_db.Forum(TimeStamp=datetime.datetime.now(), Comment='Great experience!', UserID=userOneID, PageID=resPageFifteenID)
forumFifteenID = hh_db.add_db_object(forumFifteen)

forumSixteen = hh_db.Forum(TimeStamp='2022-11-30 16:30:49.206215', Comment='They are very helpful!', UserID=userTwoID, PageID=resPageOneID)
forumSixteenID = hh_db.add_db_object(forumSixteen)
forumSeventeen = hh_db.Forum(TimeStamp='2022-11-30 16:30:49.206215', Comment='They are very helpful!', UserID=userTwoID, PageID=resPageTwoID)
forumSeventeenID = hh_db.add_db_object(forumSeventeen)

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
metricsOne = hh_db.Usage_Metrics(PageID=resPageOneID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsOneID = hh_db.add_db_object(metricsOne)
metricsTwo = hh_db.Usage_Metrics(PageID=resPageTwoID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsTwoID = hh_db.add_db_object(metricsTwo)
metricsThree = hh_db.Usage_Metrics(PageID=resPageThreeID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsThreeID = hh_db.add_db_object(metricsThree)
metricsFour = hh_db.Usage_Metrics(PageID=resPageFourID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsFourID = hh_db.add_db_object(metricsFour)
metricsFive = hh_db.Usage_Metrics(PageID=resPageFiveID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsFiveID = hh_db.add_db_object(metricsFive)
metricsSix = hh_db.Usage_Metrics(PageID=resPageSixID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsSixID = hh_db.add_db_object(metricsSix)
metricsSeven = hh_db.Usage_Metrics(PageID=resPageSevenID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsSevenID = hh_db.add_db_object(metricsSeven)
metricsEight = hh_db.Usage_Metrics(PageID=resPageEightID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsEightID = hh_db.add_db_object(metricsEight)
metricsNine = hh_db.Usage_Metrics(PageID=resPageNineID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsNineID = hh_db.add_db_object(metricsNine)
metricsTen = hh_db.Usage_Metrics(PageID=resPageTenID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsTenID = hh_db.add_db_object(metricsTen)
metricsEleven = hh_db.Usage_Metrics(PageID=resPageElevenID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsElevenID = hh_db.add_db_object(metricsEleven)
metricsTwelve = hh_db.Usage_Metrics(PageID=resPageTwelveID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsTwelveID = hh_db.add_db_object(metricsTwelve)
metricsThirteen = hh_db.Usage_Metrics(PageID=resPageThirteenID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsThirteenID = hh_db.add_db_object(metricsThirteen)
metricsFourteen = hh_db.Usage_Metrics(PageID=resPageFourteenID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsFourteenID = hh_db.add_db_object(metricsFourteen)
metricsFifteen = hh_db.Usage_Metrics(PageID=resPageFifteenID, ServicesSearched='None',
                                 NumVisitsAtRisk=0, NumVisitsVolunteer=0, NumVisitsRepresentative=0,
                                 NumVisitsOther=0, NumForumPosts=0, NumUpVotesClean=0, NumDownVotesClean=0,
                                 NumUpVotesResponsive=0, NumDownVotesResponsive=0, NumUpVotesSafe=0, NumDownVotesSafe=0)
metricsFifteenID = hh_db.add_db_object(metricsFifteen)



