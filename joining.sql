SELECT spotify.id,
  spotify.title,
  spotify.artist,
  spotify.top_genre,
  spotify.year,
  spotify.bpm,
  spotify.nrgy,
  spotify.dnce,
  spotify.db,
  spotify.live,
  spotify.val,
  spotify.dur,
  spotify.acous,
  spotify.spch,
  spotify.pop,
  grammys.category,
  grammys.nominee,
  grammys.workers,
  grammys.winner
FROM spotify
INNER JOIN grammys ON
spotify.title = grammys.nominee;

