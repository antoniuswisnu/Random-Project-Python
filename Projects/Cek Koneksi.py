from speedtest import Speedtest
st = Speedtest()
print("Koneksi Download: ", st.download())
print("Koneksi Upload: ",st.upload())
