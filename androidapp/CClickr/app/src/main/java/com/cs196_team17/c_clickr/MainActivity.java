package com.cs196_team17.c_clickr;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Context;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    public static int[] COLOR_IDS = new int[] {R.drawable.red_box, R.drawable.green_box, R.drawable.blue_box, R.drawable.yellow_box};
    private int[][] nums;

    private View[][] boxes = new View[4][4];

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        nums = new int[][]{
                {0,1,2,3},
                {3,2,1,0},
                {0,2,1,3},
                {3,0,2,1}
        };

        for (int r = 0; r < boxes.length; r++) {
            for (int c = 0; c < boxes[r].length; c++) {
                Context context = getApplicationContext();
                String boxID = "box_" + r + "_" + c;
                int id = getApplicationContext().getResources().getIdentifier(boxID, "id", context.getPackageName());
                boxes[r][c] = findViewById(id);
                boxes[r][c].setBackground(ContextCompat.getDrawable(getApplicationContext(), COLOR_IDS[nums[r][c]]));
            }
        }
    }

}
