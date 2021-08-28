import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import SkipPreviousIcon from '@material-ui/icons/SkipPrevious';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';
import SkipNextIcon from '@material-ui/icons/SkipNext';
import BackupIcon from '@material-ui/icons/Backup';
import CardActionArea from '@material-ui/core/CardActionArea';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  details: {
    display: 'flex',
    flexDirection: 'column',
  },
  content: {
    flex: '1 0 auto',
  },
  cover: {
    width: 151,
  },
  controls: {
    display: 'flex',
    alignItems: 'center',
    paddingLeft: theme.spacing(1),
    paddingBottom: theme.spacing(1),
  },
  playIcon: {
    height: 38,
    width: 38,
  },
}));

export default function MediaControlCard() {
  const classes = useStyles();
  const theme = useTheme();

  return (
    <Card>
        <CardActionArea className={classes.controls}>
          {/* <CardMedia
            className={classes.media}
            src="https://w7.pngwing.com/pngs/730/348/png-transparent-computer-icons-upload-icon-upload-miscellaneous-angle-rectangle-thumbnail.png"
            title="Contemplative Reptile"
          /> */}
            <BackupIcon fontSize='large'/>
        </CardActionArea>
        {/* <CardContent>
          <IconButton aria-label="previous">
            <BackupIcon fontSize='large'/>
          </IconButton>
        </CardContent> */}
    </Card>
  );
}
