# EEGBot
Control of Bot using neurosky mindwave headset
The project aims at detecting the ElectroEncephelpgraph Signals generated in brain during various activites.

# Electroencephalography (EEG) 
It is an electrophysiological monitoring method to record electrical activity of the brain. It is typically noninvasive, with the electrodes placed along the scalp, although invasive electrodes are sometimes used in specific applications. EEG measures voltage fluctuations resulting from ionic current within the neurons of the brain.In clinical contexts, EEG refers to the recording of the brain's spontaneous electrical activity over a period of time,as recorded from multiple electrodes placed on the scalp. Diagnostic applications generally focus on the spectral content of EEG, that is, the type of neural oscillations (popularly called "brain waves") that can be observed in EEG signals.

The attention and meditaion levels of the test subject was detected and the values obtained were used to control a bot.
The attention values were used to control the velocity of the bot. We also detected blinking of the subject and it was used to control the direction.How the values are outputted  are decribed below

# Attention
The Attention Meter algorithm indicates the intensity of mental “focus” or “attention.” The value ranges from 0 to 100. The attention level increases when a user focuses on a single thought or an external object, and decreases when distracted. Users can observe their ability to concentrate using the algorithm. In educational settings, attention to lesson plans can be tracked to measure their effectiveness in engaging students. In gaming, attention has been used to create “push” control over virtual objects.

# Meditation
The Meditation Meter algorithm indicates the level of mental “calmness” or “relaxation.” The value ranges from 0 to 100, and increases when users relax the mind and decreases when they are uneasy or stressed. The Meditation Meter quantifies the ability to find an inner state of mindfulness, and can thus help users learn how to self correct and find inner balance to overcome the stresses of everyday life. The algorithm is also used in a variety of game-design controls.

# Blink Detection
The Blink Detection algorithm signals a user’s blinks. A higher number indicates a “stronger” blink, while a smaller number indicates a “lighter” or “weaker” blink. The frequency of blinking is often correlated with nervousness or fatigue. Eye blinks are akin to a standard on/off binary system and therefore are valuable for controls that require definitive responses. For instance, in communication applications, one blink means no, two mean yes — giving individuals with a special needs a simple way to communicate.
