import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

# função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    st = speedtest.Speedtest()
    best_server = st.get_best_server()

    date_now = datetime.now().strftime('%d/%m/%Y')
    hour_now = datetime.now().strftime('%H:%M')
    download = st.download(threads=None)*(10**-6)
    upload = st.upload(threads=None)*(10**-6)
    latency = best_server['latency']

    df.loc[len(df)] = [date_now, hour_now, download, upload, latency]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)

    Timer(30, internet).start()

internet()