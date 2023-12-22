import telegram.ext
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(updater, context):
    updater.message.reply_text(
        """
        Hello!  Welcome to PES College Of Engineering..

        /help -> to get this help menu
        
        SJCE library info:
        /lib -> library info 

        I Hope this helps :)
        """)

def helps(updater, context):
    updater.message.reply_text(
        """
        Hi  there I'm Telegram bot created by students. please follow these commands:-
  
        /Start -> to start and visite college
        /about -> PES College
        /placements -> Training and Placement
        /programs -> UG and PG
        /contact -> Information about contact of college
        /help -> to get this help menu
        
        
        """
    )

def programs(update, context):
    update.message.reply_text(
        """
        /ug -> Under Graduate
        /pg -> Post Graduate
        
        """
    )

def masters(update, context):
    update.message.reply_text(
        """
        /mca -> Master of Computer Application
        /mba -> Master of Business Administration

        """
    )

def ug(update, context):
    update.message.reply_text(
    """
    /is -> Information Science and Engineering
    /cs -> computer Science and Engineering
    /ce -> Civil Engineering
    /me -> Mechnical and Engineering
    /ec -> Electronics and Communication
    /ee -> Electrical and Electronics Engineering
     
    """
    )

def pg(update, context): 
    update.message.reply_text(
    """
    /m_tech_pes -> M_TECH CSE,VLSI & ES,CIVIL
    /masters -> MCA,MBA
    """
    )

def m_tech_pes(update, context): 
    update.message.reply_text(
    """
    /m_tech_cse -> Computer Science & Engineering
    /m_tech_vlsi_es -> Electronics & Communication Engineering 
    /m_tech_civil -> Civil Engineering 
    """)

def about(update, context):
    update.message.reply_text(
        """
        PES College :-
        
        About -> Vision and Mission
        
        Vision:-:-
        "PESCE shall be a leading institution imparting quality engineering and management education developing creative and socially responsible professionals."


        Mission:-
        Provide state of the art infrastructure, motivate the faculty to be proficient in their field of specialization and adopt best teaching-learning practices.
        Impart engineering and managerial skills through competent and committed faculty using outcome based educational curriculum.
        Inculcate professional ethics, leadership qualities and entrepreneurial skills to meet the societal needs.
        Promote research, product development and industry-institution interaction.

       Quality Policy:-
       " Highly committed in providing quality, concurrent technical education and continuously striving to meet expectations of stake holders "


       Core Values:-
       Professionalism
       Empathy
       Synergy
       Commitment
       Ethics


        * Offical Website : https://pescemandya.org/
        * YouTube link : https://www.youtube.com/watch?v=qSNEez2KGmY
        """)

def ise(update, context):
    update.message.reply_text(
        """
        INFORMATION SCIENCE & ENGINEERING :-
        
        * Offical Website : https://pescemandya.org/ise/ise.php
        """)

def cs(update, context):
    update.message.reply_text(
        """
        COMPUTER SCIENCE & ENGINEERING :-

        * Offical Website : https://pescemandya.org/cse/cse.php
        """)

def lib(update, context):
    update.message.reply_text(
        """
        Sri Jayachamarajendra College of Engineering Library info:-
        
        * Offical Website : https://sjce.ac.in/academics/library-and-information-centre/
        """)

def ec(update, context):
    update.message.reply_text(
        """
        ELECTRONICS & COMMUNICATION ENGINEERING :-
        
        * Offical Website : https://pescemandya.org/ece/ece.php
        """)

def ee(update, context):
    update.message.reply_text(
        """
        ELECTRICAL & ELECTRONICS ENGINEERING :-

        * Offical Website : https://pescemandya.org/eee/eee.php
        """)

def m_tech_cse(update, context):
    update.message.reply_text(
        """
        M_TECH CSE :-
        * Offical Website : https://pescemandya.org/cse/cse.php
        """)

def m_tech_vlsi_es(update, context):
    update.message.reply_text(
        """
        M_TECH VLSI & ES :-

        * Offical Website : https://pescemandya.org/ece/ece.php
        """)

def m_tech_civil(update, context):
    update.message.reply_text(
        """
        M_TECH CIVIL :-

        * Offical Website : https://pescemandya.org/civil/civil.php
        """)

def mca(update, context):
    update.message.reply_text(
        """
        MASTERS OF COMPUTER APPLICATION :-

        * Offical Website : https://pescemandya.org/mca/mca.php
        """)

def mba(update, context):
    update.message.reply_text(
        """
        MASTERS OF BUSSINESS ADMINISTRATION :-

        * Offical Website : https://pescemandya.org/mba/mba.php
        """)

def placements(update, context):
    update.message.reply_text(
        """
        TRINING & PLACEMENT :-

        * Offical Website : https://pescemandya.org/placement/placement.php
        """) 

def contact(update, context):
    update.message.reply_text(
        """
        CONTACT IN OUR OFFICIAL WEBSITE :-
         For Admissions : 
        
        
        * Gmail : admissions@pesce.ac.in
        * Offical Website : https://pescemandya.org/contact-us.php
        """) 


def unknown_text(update, context): 
	update.message.reply_text( 
		"Sorry I can't recognize you , you said '%s'" % update.message.text) 


def unknown(update, context): 
	update.message.reply_command( 
		"Sorry '%s' is not a valid command" % update.message.command) 



updater = telegram.ext.Updater(TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))
dispatch.add_handler(telegram.ext.CommandHandler('about', about))
dispatch.add_handler(telegram.ext.CommandHandler('is', ise))
dispatch.add_handler(telegram.ext.CommandHandler('cs',cs ))
'''dispatch.add_handler(telegram.ext.CommandHandler('ce', ce)) '''
"""dispatch.add_handler(telegram.ext.CommandHandler('me', me))"""
dispatch.add_handler(telegram.ext.CommandHandler('ec', ec))
dispatch.add_handler(telegram.ext.CommandHandler('ee', ee))
dispatch.add_handler(telegram.ext.CommandHandler('m_tech_pes', m_tech_pes))
dispatch.add_handler(telegram.ext.CommandHandler('m_tech_cse', m_tech_cse))
dispatch.add_handler(telegram.ext.CommandHandler('m_tech_vlsi_es', m_tech_vlsi_es))
dispatch.add_handler(telegram.ext.CommandHandler('m_tech_civil', m_tech_civil))
dispatch.add_handler(telegram.ext.CommandHandler('mca', mca))
dispatch.add_handler(telegram.ext.CommandHandler('mba', mba))
dispatch.add_handler(telegram.ext.CommandHandler('placements', placements))
dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatch.add_handler(telegram.ext.CommandHandler('help', help))
dispatch.add_handler(telegram.ext.CommandHandler('ug', ug))
dispatch.add_handler(telegram.ext.CommandHandler('pg', pg))
dispatch.add_handler(telegram.ext.CommandHandler('masters', masters))
dispatch.add_handler(telegram.ext.CommandHandler('programs', programs))
dispatch.add_handler(telegram.ext.CommandHandler('lib', lib))


dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, unknown_text)) 
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.command, unknown)) 


updater.start_polling()
updater.idle() 

