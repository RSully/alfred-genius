#!/usr/bin/osascript -l JavaScript

function run(argv) {
    if (Application('com.apple.iTunes').running()) {
        var itunes = Application('com.apple.iTunes')
        if (itunes.playerState() === 'playing') {
            var track = itunes.currentTrack();
            return track.name() + ' ' + track.artist();
        }
    }

    if (Application('com.coppertino.Vox').running()) {
        var vox = Application('com.coppertino.Vox');
        if (vox.playerState === 1) {
            return vox.track + ' ' + vox.artist;
        }
    }
    
    // Easy to add more applications here
    
    return '';
}
