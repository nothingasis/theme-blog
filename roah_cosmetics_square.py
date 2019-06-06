from bs4 import BeautifulSoup
import json

html_doc = """<html><body><div class="l-items l-items-list l-items-btn-right l-items-offset">
          <div class="l-item l-item-minisite">
              <div class="l-item-header">Classic set *INTRO* HOLIDAY Special</div>
                <div class="l-item-details l-item-details--service-description">
                  Start from APRIL 30 end MAY 31
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours</span>
                    <span>Starting at $50</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=JN4HONRVIJ6SMHLOUHDLBXSP" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Bundle volume *INTRO* HOLIDAY Special</div>
                <div class="l-item-details l-item-details--service-description">
                  Start from April 30 end May 31
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours</span>
                    <span>Starting at $75</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=YZ2BF6YTZK7X54PNWHPQDQRQ" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Russian volume *INTRO* HOLIDAY Special </div>
                <div class="l-item-details l-item-details--service-description">
                  Start from APRIL 30 end MAY 31
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 30 minutes</span>
                    <span>Starting at $100</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=5LY7VTPLCEPWXOX4RL5RLDC4" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Classic *INTRO* Pricing</div>
                <div class="l-item-details l-item-details--service-description">
                  First time client only.
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours</span>
                    <span>$70</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=WU6MLSFXCKONN3MXPLHHRJCT" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Classic Set</div>
                <div class="l-item-details l-item-details--service-description">
                  New Lash artist (Full Set and Fills 2-4 weeks)
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>3 hours</span>
                    <span>$50</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=CDY3ATK4OLWERBMIFY2XIYJM" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Classic Fill (2 weeks)</div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>1 hour 15 minutes</span>
                    <span>$50</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=UROPFNCWSARHV2FNU6P7XV4J" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Classic Fill (3-4 weeks)</div>
                <div class="l-item-details l-item-details--service-description">
                  When past 4 weeks, you will need to get a new set. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours</span>
                    <span>$70</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=7ESNZOJSAPBGDXOJV5KZMF25" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Classic Full Set</div>
                <div class="l-item-details l-item-details--service-description">
                  Individual lash glued to 1 natural lash. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours</span>
                    <span>$120</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=POUWZLJ6WGSALIBSTVO64MFT" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Bundle volume *INTRO* Set</div>
                <div class="l-item-details l-item-details--service-description">
                  Multiple lashes applied to 1 natural lash for a more dramatic, fuller look.

*$10 for every addition hour if you want it extra full and dramatic. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 30 minutes</span>
                    <span>Starting at $85</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=S6W4BOKBG6JH7IHC3VRRFOAB" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Bundle Volume Fill (2 Weeks)</div>
                <div class="l-item-details l-item-details--service-description">
                  Multiple lashes applied to 1 natural lash for a more dramatic, fuller look.

*$10 for every addition hour if you want it extra full and dramatic. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>1 hour 45 minutes</span>
                    <span>$75</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=JB7HTNB3UKVBPLSLDJ5OQAH6" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Bundle Volume Fill (3-4 weeks)</div>
                <div class="l-item-details l-item-details--service-description">
                  $30 for every addition hour if you want it extra full and dramatic. 


******When past 4 weeks, you will need to get a new set. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 15 minutes</span>
                    <span>Starting at $90</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=JZ5HRSI7RP26M3WPBSFIVXDM" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Russian Volume *INTRO* Set</div>
                <div class="l-item-details l-item-details--service-description">
                  *First time clients only*

Fan Volume 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 30 minutes</span>
                    <span>$149</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=7DLVDRAIVGY3QSMWDLOKA3K4" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Russian Volume (Fan) </div>
                <div class="l-item-details l-item-details--service-description">
                  $30 for every addition hour if you want it extra full and dramatic. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 30 minutes</span>
                    <span>Starting at $220</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=I7BEMFNRBP7KV2R7SOOJ5KCT" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Russian Volume Fill (2 weeks)</div>
                <div class="l-item-details l-item-details--service-description">
                  $30 for every addition hour if you want it extra full and dramatic. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>1 hour 45 minutes</span>
                    <span>Starting at $100</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=MHWEXDGBDMYHFVCL7PFXZFH3" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Russian Volume Fill (3-4 weeks)</div>
                <div class="l-item-details l-item-details--service-description">
                  $30 for every addition hour if you want it extra full and dramatic. 



**** When past 4 weeks, you will need to get a new set. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 30 minutes</span>
                    <span>Starting at $125</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=KQK6R3IUYLFUWFMAABXESDLK" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Combo Volume *INTRO* Pricing</div>
                <div class="l-item-details l-item-details--service-description">
                  *First time clients only*

Our Classic Volume and Fan volume mix
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>3 hours</span>
                    <span>$130</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=JZ7SUH64RZE34J7GFSLQ5EOT" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Combo Volume Set</div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>3 hours</span>
                    <span>$200</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=UDQ2ZABJAW7KJEZYES3BSL2G" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Combo Volume (2 Weeks Fill)</div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>1 hour 45 minutes</span>
                    <span>Starting at $90</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=62BU4N6Z6UVTETI65OSZYGOA" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Combo Volume (3-4 Weeks Fill)</div>
                <div class="l-item-details l-item-details--service-description">
                  When past 4 weeks, you will need to get a new set. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>2 hours 15 minutes</span>
                    <span>Starting at $115</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=AD7IUTBG4Q7NE43QMKW3VVMT" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Lash Removal</div>
                <div class="l-item-details l-item-details--service-description">
                  Free with new lash set. 
                </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>30 minutes</span>
                    <span>$25</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=H54BDMDXKLCGCDI7AJDFDPN2" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div><div class="l-item l-item-minisite">
              <div class="l-item-header">Make up </div>
              <div class="l-item-footer">
                <div class="l-app-price">
                    <span>1 hour 30 minutes</span>
                    <span>$25</span>
                </div>
              </div>
              <div class="l-item-action">
                <a href="https://square.site/appointments/book/60bcb42e-4da5-4e35-8beb-d91bdb3f5e5b/FH4JMT69VE5JE/start?service_id=XGWGPT2CQUSPCMDZ2SZFTBL7" rel="nofollow">
                  <button class="button button--primary">Book Now</button>
                </a>
              </div>
            </div>
        </div>
        </body>
        </html>"""

soup = BeautifulSoup(html_doc, 'html.parser')

# l-item-header
# l-item-details
# l-app-price
# l-item-action

services = []
items = soup.findAll(class_='l-item')
for item in items:
    title = item.find(class_='l-item-header')
    if title is None:
        title = ''
    else:
        title = title.get_text()
    text = item.find(class_='l-item-details')
    if text is None:
        text = ''
    else:
        text = text.get_text()
    cost = item.find(class_='l-app-price')
    if cost is None:
        cost = ''
    else:
        cost = cost.get_text()

    href = item.find(class_='l-item-action')
    if href is None:
        href = ''
    else:
        href = href.a.get('href')

    services.append({
        'title': title,
        'text': text,
        'cost': cost,
        'href': href,
        'flex': 3
    })

with open('data.json', 'w') as outfile:
  json.dump(services, outfile)
