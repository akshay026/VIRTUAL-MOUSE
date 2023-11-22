import streamlit as st
import multiprocessing

#from eye import eye_movements
#from hand import GestureController
import eye
import hand


def main():
    st.title('VIRTUAL MOUSE USING HAND GESTURES AND EYE MOVEMENTS')

    if st.button('Eye Movements'):
        p = multiprocessing.Process(target=eye)
        p.start()
    elif st.button('Hand gestures'):
        p = multiprocessing.Process(target=hand)
        p.start()
    elif st.button("Terminate:"):
        p.terminate()

if __name__ == "__main__" :
    main()


