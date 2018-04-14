from wave import open
from struct import Struct
from math import floor

frame_rate = 11025
c_freq = 261.63
e_freq = 329.63
g_freq = 392.00

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
    """Write the output of a sampler function as a wav file.
    (See https://docs.python.org/3/library/wave.html)
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    out.close()

def tri(frequency, amplitude=0.3):
    """A continious triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.1):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

def mario_at(octave, z = 0):
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq / 2)
    return mario(c, e, g, low_g, z)

def mario(c, e, g, low_g, z = 0):
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/8))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/8))
    z += 1/2
    return song

def main():
    #play(both(tri(c_freq, e_freq)))
    
    #notec = note(tri(c_freq), 0, 1/4)
    #notee = note(tri(e_freq), 1/2, 1)
    #both_notes = both(notec, notee)
    #play(both_notes)
    mario_quarter =  mario_at(1/4)
    mario_2quarters = mario_at(2/4, 2)
    song = both(mario_quarter, mario_2quarters)
    mario_1 = mario_at(1, 4)
    song = both(mario_1, song)
    play(song, seconds = 6)

    return 0

if __name__ == "__main__":
    main()
