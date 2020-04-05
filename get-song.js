#!/usr/bin/osascript -l JavaScript

function run(argv) {

    try {
        if (Application('com.apple.Music').running()) {
            var musicApp = Application('com.apple.Music');
            if (musicApp.playerState() === 'playing') {
                var track = musicApp.currentTrack;
                return track.name() + ' ' + track.artist();
            }
        }
    } catch (err) { /* user on pre-catalina */ }

    try {
        if (Application('com.apple.iTunes').running()) {
            var itunes = Application('com.apple.iTunes');
            if (itunes.playerState() === 'playing') {
                var track = itunes.currentTrack;
                return track.name() + ' ' + track.artist();
            }
        }
    } catch (err) { /* user on catalina */ }

    try {
        if (Application('com.coppertino.Vox').running()) {
            var vox = Application('com.coppertino.Vox');
            if (vox.playerState() === 1) {
                return vox.track() + ' ' + vox.artist();
            }
        }
    } catch (err) { /* app may not be installed */ }
    
    // Easy to add more applications here
    
    return '';
}
