# Endpoints associated with requests to MusixMatch API.
class Endpoints:

    """Parameters:

    Authentication
        apikey: personal api key

    Objects
        track_id:               the track id
        artist_id:              the artist id
        album_id:               the album id
        commontrack_id:         the commontrack id (?)
        track_mbid:             the recording or track id
        album_mbid:             the release id

    Querying
        q_track:                search for a text string among song titles
        q_artist:               search for a text string among artist names
        q_lyrics:               search for a text string among lyrics
        q:                      search for a text string among song titles, artist names, and lyrics

    Filtering
        f_has_lyrics:                       filter by objects with available lyrics
        f_is_instrumental:                  filter instrumental songs
        f_has_subtitle:                     filter by objects with available subtitles
        f_music_genre_id:                   filter by objects with a specific music category
        f_subtitle_length:                  Filter subtitles by a given duration in seconds
        f_subtitle_length_max_deviation:    Apply a deviation to a given subtitle duration (in seconds)
        f_lyrics_language:                  Filter the tracks by lyrics language
        f_artist_id:                        Filter by objects with a given Musixmatch artist_id
        f_artist_mbid:                      Filter by objects with a given musicbrainz artist id

    Grouping
        g_commontrack:          group a track result set by commontrack_id

    Sorting
        s_track_rating:         Sort the results by our popularity index for tracks, possible values are ASC | DESC
        s_track_release_date:   Sort the results by track release date, possible values are ASC | DESC
        s_artist_rating:        Sort the results by our popularity index for artists, possible values are ASC | DESC

    Result Set Pagination
        page:                   Request specific result page (default=1)
        page_size:              Specify number of items per result page (default=10, range is 1 to 100)

    Output Format
        subtitle_format:        Desired output format for subtitle body (options: LRC (defalut), DFXP, STLEDU)

    Localization
        country:                country code of desired country
    """

    # Top charts endpoints
    class Chart:
        """
        Get the list of the top artists of a given country.

        TODO: implement params: 
            country: a valid country code (default: us), 
            page: page number for paginated results, 
            page_size: page size for paginated results (1 to 100), 
            format: the output type, json or xml (default json)
        """
        ARTISTS = "/chart.artists.get?page=1&page_size=5"

        """
        Get the list of the top songs of a given country.

        TODO: implement params: country, page, page_size, chart_name, f_has_lyrics
        """
        SONGS = "/chart.tracks.get?chart_name=top&page=1&page_size=5"