import sys
import chorderator as cdt

"""
A file that takes in a midi and outputs the accompanying instrumentation, into a folder named after the file's name. 
For example:  file name 'AccoMontage2/MIDI demos/inputs/076/melody.mid' will put the files into a folder
called '076_melody.mid_output_results' with all the midi's. 
"""





def create_instrumentation(input_melody_path):
    try: 
        parts = input_melody_path.split('/')

        # Combine the second-to-last and last parts with an underscore
        demo_name = f"{parts[-2]}_{parts[-1]}"


        cdt.set_melody(input_melody_path)
        print('melody')
        cdt.set_meta(tonic=cdt.Key.G)
        cdt.set_segmentation('A8B8A8B8')
        print('segmentation')


        cdt.set_texture_prefilter((0, 2))

        cdt.set_note_shift(0)
        print('note shift')


        cdt.set_output_style(cdt.Style.POP_STANDARD)

        cdt.generate_save(demo_name + '_output_results')
        print(demo_name + '_output_results')

    except Exception as e: 
        print(e)
        return e

    return demo_name + '_output_results'+'/chord_gen.mid'