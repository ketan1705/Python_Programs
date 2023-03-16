from speedtest import Speedtest
st=Speedtest()
print("Your connection download speed is:",st.download())
print("Your connection upload speed is:",st.upload())