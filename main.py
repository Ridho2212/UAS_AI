import streamlit as st

#membuat background
page_bg_img = """
<style> 
.block-container.css-91z34k.egzxvld4{
    background-color: white;
    margin-top: 50px;
    border-radius: 15px;
    height: 1200px;
}
.stApp.css-fg4pbf.eczokvf1{
    background-color: #e5e5f7;
    opacity: 0.8;
    background-image:  linear-gradient(#444cf7 1.6px, transparent 1.6px), linear-gradient(to right, #444cf7 1.6px, #e5e5f7 1.6px);
    background-size: 32px 32px;
}
.nav.nav-pills.mb-auto.nav-justified{
    margin-top: -100px;
}
img{
    margin-top: -110px;
    margin-left: 100px;
}


</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
################################################

# Menghapus watermark dari library
st.markdown("""
<style>
#MainMenu{
    visibility: hidden;
}   
.css-h5rgaw.egzxvld1{
    visibility: hidden;
}
.css-18ni7ap.e8zbici2{
    visibility: hidden; 
}
</style>      
""",unsafe_allow_html=True)

from PIL import Image
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from streamlit_option_menu import option_menu
#NLTK Packages 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

#Fuctionforsumy
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 1)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


#Function for NLTK 
def nltk_summarizer(docx):
    stopWords = set(stopwords.words("indonesian")) 
    words = word_tokenize(docx) 
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1
       
    sentences = sent_tokenize(docx) 
    sentenceValue = dict() 
   
    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq 
                    
    sumValues = 0
    
#Memasukkan Logo Aplikasi
image = Image.open('logo.jpeg')
st.image(image, caption='', width=500)
def main():

    #Membuat Navigasi
    selected = option_menu(
        menu_title=None,
        options=["Home","About","Contac"],
        icons=["house","book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    
   
    st.subheader("Aplikasi Rangkuman Text Sederhana")

    if 'Halaman Rangkuman':
        raw_text = st.text_area("Masukkan Teks Disini","")
    if st.button("Ringkas Sekarang"):
        if 'Halaman Ringkasan Teks':
            summary_result = sumy_summarizer(raw_text)

        st.caption("Berikut Hasil Rangkuman Teks")
        st.info(summary_result)
        st.button("Hapus Ringkasan", "#")
        

        
if __name__ == '__main__':
    main()
    
    #Menambahkan Artikel
    st.subheader("Alat Meringkas")
    st.caption("Peringkas teks adalah alat online yang membungkus teks dengan panjang pendek tertentu Ini memadatkan artikel panjang ke poin utama Kebutuhan akan peringkas teks semakin meningkat dari hari ke hari, karena keterbatasan waktu. Orang mencari cara pintas untuk mempelajari ide dalam waktu yang lebih singkat. Bahkan peringkasan teks membantu mereka memutuskan apakah sebuah buku, makalah penelitian, atau artikel layak dibaca atau tidak. Oxford mendefinisikan ringkasan sebagai:pernyataan singkat yang hanya memberikan poin utama dari sesuatu, bukan detailnya. ") 
    st.subheader("Bagaimana cara kerja rangkuman online ini?")
    st.caption("Dilatih oleh pembelajaran mesin, peringkas teks ini menggunakan konsep peringkasan abstrak untuk meringkas buku, artikel, atau makalah penelitian.Ini menggunakan NLP untuk membuat kalimat baru dan menghasilkan ringkasan di mana ide utama tetap utuh. TI adalah alat tingkat lanjut yang menggunakan AI untuk pekerjaannya. Oleh karena itu, ringkasan yang dihasilkan oleh alat ini tampak sempurna dan mengalir.")
    st.subheader("Bagaimana cara menggunakan peringkas teks kami?")
    st.caption("Alat peringkasan kami adalah yang terbaik karena mudah digunakan dan juga efisien 1.Masukkan teks artikel ke dalam area teks. 2. Klik tombol Ringkas Sekarang. 3.Selamat anda sudah bisa meringkas dokumen anda")
  
#Membuat footer  
st.markdown("""
<style>
.footer {
    padding: 10px;
    width: 100%;
    background-color: #FF4B4B;
    color: white;
    text-align: center;
    margin-top: 30px;
}
</style>

<div class="footer">
    <p>Copyright &copy; Kelompok <u><b>PTB</b></u> Nurul Fikri</p>
</div>
</styl>      
""",unsafe_allow_html=True)

